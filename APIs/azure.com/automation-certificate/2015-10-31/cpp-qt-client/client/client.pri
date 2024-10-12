QT += network

HEADERS += \
# Models
    $${PWD}/OAICertificate.h \
    $${PWD}/OAICertificateCreateOrUpdateParameters.h \
    $${PWD}/OAICertificateCreateOrUpdateProperties.h \
    $${PWD}/OAICertificateListResult.h \
    $${PWD}/OAICertificateProperties.h \
    $${PWD}/OAICertificateUpdateParameters.h \
    $${PWD}/OAICertificateUpdateProperties.h \
    $${PWD}/OAICertificate_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAICertificateApi.h \
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
    $${PWD}/OAICertificate.cpp \
    $${PWD}/OAICertificateCreateOrUpdateParameters.cpp \
    $${PWD}/OAICertificateCreateOrUpdateProperties.cpp \
    $${PWD}/OAICertificateListResult.cpp \
    $${PWD}/OAICertificateProperties.cpp \
    $${PWD}/OAICertificateUpdateParameters.cpp \
    $${PWD}/OAICertificateUpdateProperties.cpp \
    $${PWD}/OAICertificate_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAICertificateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
