QT += network

HEADERS += \
# Models
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIProductResource.h \
    $${PWD}/OAIProductResourcesPage.h \
    $${PWD}/OAIProduct_allOf_compatibility.h \
    $${PWD}/OAIProduct_allOf_iconUris.h \
    $${PWD}/OAIProduct_allOf_productProperties.h \
    $${PWD}/OAIProducts_Download_200_response.h \
    $${PWD}/OAIProducts_Download_200_response_properties.h \
    $${PWD}/OAIProducts_Download_200_response_properties_links_inner.h \
# APIs
    $${PWD}/OAIProductsApi.h \
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
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIProductResource.cpp \
    $${PWD}/OAIProductResourcesPage.cpp \
    $${PWD}/OAIProduct_allOf_compatibility.cpp \
    $${PWD}/OAIProduct_allOf_iconUris.cpp \
    $${PWD}/OAIProduct_allOf_productProperties.cpp \
    $${PWD}/OAIProducts_Download_200_response.cpp \
    $${PWD}/OAIProducts_Download_200_response_properties.cpp \
    $${PWD}/OAIProducts_Download_200_response_properties_links_inner.cpp \
# APIs
    $${PWD}/OAIProductsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
