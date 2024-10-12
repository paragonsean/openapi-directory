QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutoscaleNotification.h \
    $${PWD}/OAIAutoscaleProfile.h \
    $${PWD}/OAIAutoscaleSetting.h \
    $${PWD}/OAIAutoscaleSettingResource.h \
    $${PWD}/OAIAutoscaleSettingResourceCollection.h \
    $${PWD}/OAIAutoscaleSettingResourcePatch.h \
    $${PWD}/OAIEmailNotification.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIMetricTrigger.h \
    $${PWD}/OAIRecurrence.h \
    $${PWD}/OAIRecurrentSchedule.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIScaleAction.h \
    $${PWD}/OAIScaleCapacity.h \
    $${PWD}/OAIScaleRule.h \
    $${PWD}/OAITimeWindow.h \
    $${PWD}/OAIWebhookNotification.h \
# APIs
    $${PWD}/OAIAutoscaleSettingsApi.h \
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAutoscaleNotification.cpp \
    $${PWD}/OAIAutoscaleProfile.cpp \
    $${PWD}/OAIAutoscaleSetting.cpp \
    $${PWD}/OAIAutoscaleSettingResource.cpp \
    $${PWD}/OAIAutoscaleSettingResourceCollection.cpp \
    $${PWD}/OAIAutoscaleSettingResourcePatch.cpp \
    $${PWD}/OAIEmailNotification.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIMetricTrigger.cpp \
    $${PWD}/OAIRecurrence.cpp \
    $${PWD}/OAIRecurrentSchedule.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIScaleAction.cpp \
    $${PWD}/OAIScaleCapacity.cpp \
    $${PWD}/OAIScaleRule.cpp \
    $${PWD}/OAITimeWindow.cpp \
    $${PWD}/OAIWebhookNotification.cpp \
# APIs
    $${PWD}/OAIAutoscaleSettingsApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
