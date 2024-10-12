QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvancedSchedule.h \
    $${PWD}/OAIAdvancedScheduleMonthlyOccurrence.h \
    $${PWD}/OAIAzureQueryProperties.h \
    $${PWD}/OAICollectionItemUpdateConfiguration.h \
    $${PWD}/OAILinuxProperties.h \
    $${PWD}/OAINonAzureQueryProperties.h \
    $${PWD}/OAIOperatingSystemType.h \
    $${PWD}/OAIScheduleProperties.h \
    $${PWD}/OAISoftwareUpdateConfiguration.h \
    $${PWD}/OAISoftwareUpdateConfigurationCollectionItem.h \
    $${PWD}/OAISoftwareUpdateConfigurationCollectionItemProperties.h \
    $${PWD}/OAISoftwareUpdateConfigurationListResult.h \
    $${PWD}/OAISoftwareUpdateConfigurationProperties.h \
    $${PWD}/OAISoftwareUpdateConfigurationTasks.h \
    $${PWD}/OAISoftwareUpdateConfigurations_List_default_response.h \
    $${PWD}/OAITagSettingsProperties.h \
    $${PWD}/OAITargetProperties.h \
    $${PWD}/OAITaskProperties.h \
    $${PWD}/OAIUpdateConfiguration.h \
    $${PWD}/OAIWindowsProperties.h \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationApi.h \
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
    $${PWD}/OAIAdvancedSchedule.cpp \
    $${PWD}/OAIAdvancedScheduleMonthlyOccurrence.cpp \
    $${PWD}/OAIAzureQueryProperties.cpp \
    $${PWD}/OAICollectionItemUpdateConfiguration.cpp \
    $${PWD}/OAILinuxProperties.cpp \
    $${PWD}/OAINonAzureQueryProperties.cpp \
    $${PWD}/OAIOperatingSystemType.cpp \
    $${PWD}/OAIScheduleProperties.cpp \
    $${PWD}/OAISoftwareUpdateConfiguration.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationCollectionItem.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationCollectionItemProperties.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationListResult.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationProperties.cpp \
    $${PWD}/OAISoftwareUpdateConfigurationTasks.cpp \
    $${PWD}/OAISoftwareUpdateConfigurations_List_default_response.cpp \
    $${PWD}/OAITagSettingsProperties.cpp \
    $${PWD}/OAITargetProperties.cpp \
    $${PWD}/OAITaskProperties.cpp \
    $${PWD}/OAIUpdateConfiguration.cpp \
    $${PWD}/OAIWindowsProperties.cpp \
# APIs
    $${PWD}/OAISoftwareUpdateConfigurationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
