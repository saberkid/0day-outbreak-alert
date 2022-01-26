import imp
import scripts.utils as utils
import datetime
import common.const as const
import time
import copy
from model.db_helper import setup_db
from model.import_record import ImportRecord

def prepare_data(cve, start_date, db_session):
    end_date = copy.deepcopy(start_date)
    for i in range(const.MONITORING_DAYS):
        end_date = end_date + datetime.timedelta(days=1)
        res = utils.url_news_search(cve, start_date, end_date)
        record = ImportRecord()
        record.count = res
        record.cve = cve
        record.start_datetime = start_date
        record.end_datetime = end_date
        db_session.add(record)
        db_session.flush()
        time.sleep(const.REQUEST_INTERVAL)
    db_session.commit()


def search_known_exploits(cutoff_date="20200101"):
    cutoff_date = datetime.datetime.strptime(cutoff_date, '%Y%m%d')
    known_list = utils.get_known_exploits()
    engine, Session = setup_db("database.db")
    db_session = Session()

    for exploit in known_list['vulnerabilities']:
        cve = exploit['cveID']
        created_date = utils.query_cve_created_date(cve)
        if created_date and created_date > cutoff_date:
            prepare_data(cve, created_date, db_session)
        # break

search_known_exploits()