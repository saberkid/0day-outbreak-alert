import utils
import datetime


def prepare_data(cve, start_date):
    pass


def search_known_exploits(cutoff_date="20200101"):
    cutoff_date = datetime.datetime.strptime(cutoff_date, '%Y%m%d')
    known_list = utils.get_known_exploits()
    for exploit in known_list['vulnerabilities']:
        cve = exploit['cveID']
        created_date = utils.query_cve_created_date(cve)
        if created_date and created_date > cutoff_date:
            prepare_data(cve, created_date)
