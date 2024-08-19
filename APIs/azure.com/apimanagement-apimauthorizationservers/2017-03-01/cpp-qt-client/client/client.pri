QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorizationServerCollection.h \
    $${PWD}/OAIAuthorizationServerContract.h \
    $${PWD}/OAIAuthorizationServerContractBaseProperties.h \
    $${PWD}/OAIAuthorizationServerContractProperties.h \
    $${PWD}/OAIAuthorizationServerUpdateContract.h \
    $${PWD}/OAIAuthorizationServerUpdateContractProperties.h \
    $${PWD}/OAIAuthorizationServer_Get_default_response.h \
    $${PWD}/OAIAuthorizationServer_Get_default_response_details_inner.h \
    $${PWD}/OAITokenBodyParameterContract.h \
# APIs
    $${PWD}/OAIAuthorizationServersApi.h \
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
    $${PWD}/OAIAuthorizationServerCollection.cpp \
    $${PWD}/OAIAuthorizationServerContract.cpp \
    $${PWD}/OAIAuthorizationServerContractBaseProperties.cpp \
    $${PWD}/OAIAuthorizationServerContractProperties.cpp \
    $${PWD}/OAIAuthorizationServerUpdateContract.cpp \
    $${PWD}/OAIAuthorizationServerUpdateContractProperties.cpp \
    $${PWD}/OAIAuthorizationServer_Get_default_response.cpp \
    $${PWD}/OAIAuthorizationServer_Get_default_response_details_inner.cpp \
    $${PWD}/OAITokenBodyParameterContract.cpp \
# APIs
    $${PWD}/OAIAuthorizationServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
