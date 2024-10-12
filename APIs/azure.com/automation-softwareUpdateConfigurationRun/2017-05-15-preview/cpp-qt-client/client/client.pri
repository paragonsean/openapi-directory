QT += network

HEADERS += \
# Models
    $${PWD}/OAISoftareUpdateConfigurationRunTaskProperties.h \
    $${PWD}/OAISoftareUpdateConfigurationRunTasks.h \
    $${PWD}/OAISoftwareUpdateConfigurationRun.h \
    $${PWD}/OAISoftwareUpdateConfigurationRunListResult.h \
    $${PWD}/OAISoftwareUpdateConfigurationRunProperties.h \
    $${PWD}/OAISoftwareUpdateConfigurationRuns_List_default_response.h \
    $${PWD}/OAIUpdateConfigurationNavigation.h \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationRunApi.h \
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
    $${PWD}/OAISoftareUpdateConfigurationRunTaskProperties.cpp \
    $${PWD}/OAISoftareUpdateConfigurationRunTasks.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationRun.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationRunListResult.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationRunProperties.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationRuns_List_default_response.cpp \
    $${PWD}/OAIUpdateConfigurationNavigation.cpp \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationRunApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
