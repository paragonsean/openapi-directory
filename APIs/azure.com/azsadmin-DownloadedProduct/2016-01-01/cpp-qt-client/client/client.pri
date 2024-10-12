QT += network

HEADERS += \
# Models
    $${PWD}/OAIDownloadedProductResourcesPage.h \
    $${PWD}/OAIDownloadedProductResourcesPage_value_inner.h \
    $${PWD}/OAIDownloadedProducts_Get_200_response.h \
    $${PWD}/OAIDownloadedProducts_Get_200_response_properties.h \
    $${PWD}/OAIDownloadedProducts_Get_200_response_properties_links_inner.h \
# APIs
    $${PWD}/OAIDownloadedProductsApi.h \
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
    $${PWD}/OAIDownloadedProductResourcesPage.cpp \
    $${PWD}/OAIDownloadedProductResourcesPage_value_inner.cpp \
    $${PWD}/OAIDownloadedProducts_Get_200_response.cpp \
    $${PWD}/OAIDownloadedProducts_Get_200_response_properties.cpp \
    $${PWD}/OAIDownloadedProducts_Get_200_response_properties_links_inner.cpp \
# APIs
    $${PWD}/OAIDownloadedProductsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
