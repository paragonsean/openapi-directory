QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Catalog.h \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Product.h \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse.h \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchProductsResponse.h \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchVersionsResponse.h \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Version.h \
# APIs
    $${PWD}/OAIOrganizationsApi.h \
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
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Catalog.cpp \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Product.cpp \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse.cpp \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchProductsResponse.cpp \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1SearchVersionsResponse.cpp \
    $${PWD}/OAIGoogleCloudPrivatecatalogV1beta1Version.cpp \
# APIs
    $${PWD}/OAIOrganizationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
