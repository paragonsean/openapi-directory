QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateNotificationConfigurationRequest.h \
    $${PWD}/OAIDeleteNotificationConfigurationRequest.h \
    $${PWD}/OAIErrorFieldType.h \
    $${PWD}/OAIExchangeMessage.h \
    $${PWD}/OAIFieldType.h \
    $${PWD}/OAIGenericResponse.h \
    $${PWD}/OAIGetNotificationConfigurationListResponse.h \
    $${PWD}/OAIGetNotificationConfigurationRequest.h \
    $${PWD}/OAIGetNotificationConfigurationResponse.h \
    $${PWD}/OAINotificationConfigurationDetails.h \
    $${PWD}/OAINotificationEventConfiguration.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAITestNotificationConfigurationRequest.h \
    $${PWD}/OAITestNotificationConfigurationResponse.h \
    $${PWD}/OAIUpdateNotificationConfigurationRequest.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAICreateNotificationConfigurationRequest.cpp \
    $${PWD}/OAIDeleteNotificationConfigurationRequest.cpp \
    $${PWD}/OAIErrorFieldType.cpp \
    $${PWD}/OAIExchangeMessage.cpp \
    $${PWD}/OAIFieldType.cpp \
    $${PWD}/OAIGenericResponse.cpp \
    $${PWD}/OAIGetNotificationConfigurationListResponse.cpp \
    $${PWD}/OAIGetNotificationConfigurationRequest.cpp \
    $${PWD}/OAIGetNotificationConfigurationResponse.cpp \
    $${PWD}/OAINotificationConfigurationDetails.cpp \
    $${PWD}/OAINotificationEventConfiguration.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAITestNotificationConfigurationRequest.cpp \
    $${PWD}/OAITestNotificationConfigurationResponse.cpp \
    $${PWD}/OAIUpdateNotificationConfigurationRequest.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
