QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiCollection.h \
    $${PWD}/OAIApiContract.h \
    $${PWD}/OAIApiEntityBaseContract.h \
    $${PWD}/OAIApiExportResult.h \
    $${PWD}/OAIApiProducts_ListByApis_200_response.h \
    $${PWD}/OAIApiProducts_ListByApis_200_response_value_inner.h \
    $${PWD}/OAIApiUpdateContract.h \
    $${PWD}/OAIApis_ListByService_default_response.h \
    $${PWD}/OAIApis_ListByService_default_response_details_inner.h \
    $${PWD}/OAIAuthenticationSettingsContract.h \
    $${PWD}/OAIOAuth2AuthenticationSettingsContract.h \
    $${PWD}/OAIOperationCollection.h \
    $${PWD}/OAIOperationContract.h \
    $${PWD}/OAIOperationEntityBaseContract.h \
    $${PWD}/OAIOperationUpdateContract.h \
    $${PWD}/OAIParameterContract.h \
    $${PWD}/OAIRepresentationContract.h \
    $${PWD}/OAIRequestContract.h \
    $${PWD}/OAIResultContract.h \
    $${PWD}/OAISubscriptionKeyParameterNamesContract.h \
# APIs
    $${PWD}/OAIApiOperationsPolicyApi.h \
    $${PWD}/OAIApiPolicyApi.h \
    $${PWD}/OAIApiProductsApi.h \
    $${PWD}/OAIApisApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIApiCollection.cpp \
    $${PWD}/OAIApiContract.cpp \
    $${PWD}/OAIApiEntityBaseContract.cpp \
    $${PWD}/OAIApiExportResult.cpp \
    $${PWD}/OAIApiProducts_ListByApis_200_response.cpp \
    $${PWD}/OAIApiProducts_ListByApis_200_response_value_inner.cpp \
    $${PWD}/OAIApiUpdateContract.cpp \
    $${PWD}/OAIApis_ListByService_default_response.cpp \
    $${PWD}/OAIApis_ListByService_default_response_details_inner.cpp \
    $${PWD}/OAIAuthenticationSettingsContract.cpp \
    $${PWD}/OAIOAuth2AuthenticationSettingsContract.cpp \
    $${PWD}/OAIOperationCollection.cpp \
    $${PWD}/OAIOperationContract.cpp \
    $${PWD}/OAIOperationEntityBaseContract.cpp \
    $${PWD}/OAIOperationUpdateContract.cpp \
    $${PWD}/OAIParameterContract.cpp \
    $${PWD}/OAIRepresentationContract.cpp \
    $${PWD}/OAIRequestContract.cpp \
    $${PWD}/OAIResultContract.cpp \
    $${PWD}/OAISubscriptionKeyParameterNamesContract.cpp \
# APIs
    $${PWD}/OAIApiOperationsPolicyApi.cpp \
    $${PWD}/OAIApiPolicyApi.cpp \
    $${PWD}/OAIApiProductsApi.cpp \
    $${PWD}/OAIApisApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
