QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiTagResourceContractProperties.h \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings.h \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings_oAuth2.h \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings_openid.h \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_subscriptionKeyParameterNames.h \
    $${PWD}/OAIOperationTagResourceContractProperties.h \
    $${PWD}/OAIProductTagResourceContractProperties.h \
    $${PWD}/OAITagResourceCollection.h \
    $${PWD}/OAITagResourceContract.h \
    $${PWD}/OAITagTagResourceContractProperties.h \
# APIs
    $${PWD}/OAITagResourcesApi.h \
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
    $${PWD}/OAIApiTagResourceContractProperties.cpp \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings.cpp \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings_oAuth2.cpp \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_authenticationSettings_openid.cpp \
    $${PWD}/OAIApiTagResourceContractProperties_allOf_subscriptionKeyParameterNames.cpp \
    $${PWD}/OAIOperationTagResourceContractProperties.cpp \
    $${PWD}/OAIProductTagResourceContractProperties.cpp \
    $${PWD}/OAITagResourceCollection.cpp \
    $${PWD}/OAITagResourceContract.cpp \
    $${PWD}/OAITagTagResourceContractProperties.cpp \
# APIs
    $${PWD}/OAITagResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
