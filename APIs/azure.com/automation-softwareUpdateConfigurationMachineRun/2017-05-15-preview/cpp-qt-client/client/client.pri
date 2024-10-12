QT += network

HEADERS += \
# Models
    $${PWD}/OAIJobNavigation.h \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRun.h \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRunListResult.h \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRuns_List_default_response.h \
    $${PWD}/OAIUpdateConfigurationMachineRunProperties.h \
    $${PWD}/OAIUpdateConfigurationNavigation.h \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationMachineRunApi.h \
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
    $${PWD}/OAIJobNavigation.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRun.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRunListResult.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationMachineRuns_List_default_response.cpp \
    $${PWD}/OAIUpdateConfigurationMachineRunProperties.cpp \
    $${PWD}/OAIUpdateConfigurationNavigation.cpp \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationMachineRunApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
