import os
import sys
import datetime

from util.config import (get_sonar_config_file, get_cli_params)
from sonar.sonar import (export_all_sonar_users, export_all_sonar_groups, export_all_sonar_groups_members, export_all_sonar_projects, export_all_sonar_projects_metrics, export_all_sonar_projects_analyses, export_all_sonar_projects_analyses_metrics, export_all_sonar_projects_quality_gates, export_all_sonar_projects_analyses_qg, get_all_sonar_projects)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get command line parameters
    config_file, action = get_cli_params(sys.argv[1:])

    # Create the export and/or config directories if doesnt exists
    export_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/export/"
    config_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/config/"
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    if not os.path.exists(export_path):
        os.makedirs(export_path)
        print("{} - INFO - The directory ""{}"" has been created".format(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"), export_path))
    if not os.path.exists(config_path):
        os.makedirs(config_path)
        print("{} - INFO - The directory ""{}"" has been created".format(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"), config_path))


    # Execute the action requested
    if action == "export_all_sonar_users":
        sonar_site, sonar_protocol, sonar_domain_name, sonar_token = get_sonar_config_file(config_path + config_file)
        export_all_sonar_users(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, export_path + "{}-sonar-users-{}.csv".format(current_date, sonar_site))

    elif action == "export_all_sonar_groups_and_members":
        sonar_site, sonar_protocol, sonar_domain_name, sonar_token = get_sonar_config_file(config_path + config_file)
        groups_list = export_all_sonar_groups(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, export_path + "{}-sonar-groups-{}.csv".format(current_date, sonar_site))
        export_all_sonar_groups_members(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, groups_list, export_path + "{}-sonar-groups-members-{}.csv".format(current_date, sonar_site))

    elif action == "export_all_sonar_projects_with_metrics":
        sonar_site, sonar_protocol, sonar_domain_name, sonar_token = get_sonar_config_file(config_path + config_file)
        projects_list = export_all_sonar_projects(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, export_path + "{}-sonar-projects-{}.csv".format(current_date, sonar_site))
        export_all_sonar_projects_metrics(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, projects_list, export_path + "{}-sonar-projects-metrics-{}.csv".format(current_date, sonar_site))
        export_all_sonar_projects_quality_gates(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, projects_list, export_path + "{}-sonar-projects-quality-gates-{}.csv".format(current_date, sonar_site))

    elif action == "export_all_sonar_projects_analyses":
        sonar_site, sonar_protocol, sonar_domain_name, sonar_token = get_sonar_config_file(config_path + config_file)
        projects_list = get_all_sonar_projects(sonar_site, sonar_protocol, sonar_domain_name, sonar_token)
        export_all_sonar_projects_analyses(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, projects_list, export_path + "{}-sonar-projects-analyses-{}.csv".format(current_date, sonar_site))
        export_all_sonar_projects_analyses_qg(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, projects_list, export_path + "{}-sonar-projects-analyses-qg-{}.csv".format(current_date, sonar_site))

    elif action == "export_all_sonar_projects_analyses_metrics":
        sonar_site, sonar_protocol, sonar_domain_name, sonar_token = get_sonar_config_file(config_path + config_file)
        export_all_sonar_projects_analyses_metrics(sonar_site, sonar_protocol, sonar_domain_name, sonar_token, export_path + "{}-sonar-analyses-metrics-{}.csv".format(current_date, sonar_site))
