QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplication.h \
    $${PWD}/OAIApplicationBase.h \
    $${PWD}/OAIApplicationCreated.h \
    $${PWD}/OAIApplications.h \
    $${PWD}/OAIApplicationsBase.h \
    $${PWD}/OAIApplicationsBase__embedded.h \
    $${PWD}/OAICreateApplication_request.h \
    $${PWD}/OAIKeys.h \
    $${PWD}/OAIKeysWithPrivateKey.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMessages.h \
    $${PWD}/OAIMessages_webhooks_inner.h \
    $${PWD}/OAIUpdateApplication_request.h \
    $${PWD}/OAIVoice.h \
    $${PWD}/OAIVoice_webhooks_inner.h \
# APIs
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
    $${PWD}/OAIApplication.cpp \
    $${PWD}/OAIApplicationBase.cpp \
    $${PWD}/OAIApplicationCreated.cpp \
    $${PWD}/OAIApplications.cpp \
    $${PWD}/OAIApplicationsBase.cpp \
    $${PWD}/OAIApplicationsBase__embedded.cpp \
    $${PWD}/OAICreateApplication_request.cpp \
    $${PWD}/OAIKeys.cpp \
    $${PWD}/OAIKeysWithPrivateKey.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMessages.cpp \
    $${PWD}/OAIMessages_webhooks_inner.cpp \
    $${PWD}/OAIUpdateApplication_request.cpp \
    $${PWD}/OAIVoice.cpp \
    $${PWD}/OAIVoice_webhooks_inner.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
