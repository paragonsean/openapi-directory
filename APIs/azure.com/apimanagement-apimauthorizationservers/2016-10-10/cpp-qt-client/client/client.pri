QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorizationServerCollection.h \
    $${PWD}/OAIAuthorizationServers_Get_default_response.h \
    $${PWD}/OAIAuthorizationServers_Get_default_response_details_inner.h \
    $${PWD}/OAIOAuth2AuthorizationServerContract.h \
    $${PWD}/OAIOAuth2AuthorizationServerUpdateContract.h \
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
    $${PWD}/OAIAuthorizationServers_Get_default_response.cpp \
    $${PWD}/OAIAuthorizationServers_Get_default_response_details_inner.cpp \
    $${PWD}/OAIOAuth2AuthorizationServerContract.cpp \
    $${PWD}/OAIOAuth2AuthorizationServerUpdateContract.cpp \
    $${PWD}/OAITokenBodyParameterContract.cpp \
# APIs
    $${PWD}/OAIAuthorizationServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
