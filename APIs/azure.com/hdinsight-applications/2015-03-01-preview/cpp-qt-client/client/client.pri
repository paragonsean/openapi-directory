QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplication.h \
    $${PWD}/OAIApplicationGetEndpoint.h \
    $${PWD}/OAIApplicationGetHttpsEndpoint.h \
    $${PWD}/OAIApplicationListResult.h \
    $${PWD}/OAIApplicationProperties.h \
    $${PWD}/OAIApplicationProperties_computeProfile.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_capacity.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_hardwareProfile.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_scriptActions_inner.h \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_virtualNetworkProfile.h \
    $${PWD}/OAIApplicationProperties_errors_inner.h \
    $${PWD}/OAIApplicationProperties_installScriptActions_inner.h \
    $${PWD}/OAIApplications_List_default_response.h \
# APIs
    $${PWD}/OAIApplicationsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIApplication.cpp \
    $${PWD}/OAIApplicationGetEndpoint.cpp \
    $${PWD}/OAIApplicationGetHttpsEndpoint.cpp \
    $${PWD}/OAIApplicationListResult.cpp \
    $${PWD}/OAIApplicationProperties.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_capacity.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_hardwareProfile.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_scriptActions_inner.cpp \
    $${PWD}/OAIApplicationProperties_computeProfile_roles_inner_virtualNetworkProfile.cpp \
    $${PWD}/OAIApplicationProperties_errors_inner.cpp \
    $${PWD}/OAIApplicationProperties_installScriptActions_inner.cpp \
    $${PWD}/OAIApplications_List_default_response.cpp \
# APIs
    $${PWD}/OAIApplicationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
