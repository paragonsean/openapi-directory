QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperationEntityContract.h \
    $${PWD}/OAIOperationEntityContractProperties.h \
    $${PWD}/OAITagResourceCollection.h \
    $${PWD}/OAITagResourceContract.h \
    $${PWD}/OAITagResourceContractProperties.h \
    $${PWD}/OAITagResourceContractProperties_api.h \
    $${PWD}/OAITagResourceContractProperties_api_properties.h \
    $${PWD}/OAITagResourceContractProperties_api_properties_apiVersionSet.h \
    $${PWD}/OAITagResourceContractProperties_api_properties_apiVersionSet_properties.h \
    $${PWD}/OAITagResourceContractProperties_product.h \
    $${PWD}/OAITagResourceContractProperties_product_properties.h \
    $${PWD}/OAITagResourceContractProperties_tag.h \
    $${PWD}/OAITagResourceContractProperties_tag_properties.h \
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
    $${PWD}/OAIOperationEntityContract.cpp \
    $${PWD}/OAIOperationEntityContractProperties.cpp \
    $${PWD}/OAITagResourceCollection.cpp \
    $${PWD}/OAITagResourceContract.cpp \
    $${PWD}/OAITagResourceContractProperties.cpp \
    $${PWD}/OAITagResourceContractProperties_api.cpp \
    $${PWD}/OAITagResourceContractProperties_api_properties.cpp \
    $${PWD}/OAITagResourceContractProperties_api_properties_apiVersionSet.cpp \
    $${PWD}/OAITagResourceContractProperties_api_properties_apiVersionSet_properties.cpp \
    $${PWD}/OAITagResourceContractProperties_product.cpp \
    $${PWD}/OAITagResourceContractProperties_product_properties.cpp \
    $${PWD}/OAITagResourceContractProperties_tag.cpp \
    $${PWD}/OAITagResourceContractProperties_tag_properties.cpp \
# APIs
    $${PWD}/OAITagResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
