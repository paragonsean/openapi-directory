QT += network

HEADERS += \
# Models
    $${PWD}/OAICredential.h \
    $${PWD}/OAICredentialCreateOrUpdateParameters.h \
    $${PWD}/OAICredentialCreateOrUpdateProperties.h \
    $${PWD}/OAICredentialListResult.h \
    $${PWD}/OAICredentialProperties.h \
    $${PWD}/OAICredentialUpdateParameters.h \
    $${PWD}/OAICredentialUpdateProperties.h \
    $${PWD}/OAICredential_Get_default_response.h \
# APIs
    $${PWD}/OAICredentialApi.h \
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
    $${PWD}/OAICredential.cpp \
    $${PWD}/OAICredentialCreateOrUpdateParameters.cpp \
    $${PWD}/OAICredentialCreateOrUpdateProperties.cpp \
    $${PWD}/OAICredentialListResult.cpp \
    $${PWD}/OAICredentialProperties.cpp \
    $${PWD}/OAICredentialUpdateParameters.cpp \
    $${PWD}/OAICredentialUpdateProperties.cpp \
    $${PWD}/OAICredential_Get_default_response.cpp \
# APIs
    $${PWD}/OAICredentialApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
