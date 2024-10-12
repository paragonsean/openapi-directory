QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIPublicSubscriptionStatus.h \
    $${PWD}/OAIPublicSubscriptionStatusesResponse.h \
    $${PWD}/OAIPublicUpdateSubscriptionStatusRequest.h \
    $${PWD}/OAISubscriptionDefinition.h \
    $${PWD}/OAISubscriptionDefinitionsResponse.h \
# APIs
    $${PWD}/OAIDefinitionApi.h \
    $${PWD}/OAIStatusApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIPublicSubscriptionStatus.cpp \
    $${PWD}/OAIPublicSubscriptionStatusesResponse.cpp \
    $${PWD}/OAIPublicUpdateSubscriptionStatusRequest.cpp \
    $${PWD}/OAISubscriptionDefinition.cpp \
    $${PWD}/OAISubscriptionDefinitionsResponse.cpp \
# APIs
    $${PWD}/OAIDefinitionApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
