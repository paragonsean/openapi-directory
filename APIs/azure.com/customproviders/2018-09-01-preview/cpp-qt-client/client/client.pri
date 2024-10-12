QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssociation.h \
    $${PWD}/OAIAssociation_properties.h \
    $${PWD}/OAIAssociationsList.h \
    $${PWD}/OAICustomRPActionRouteDefinition.h \
    $${PWD}/OAICustomRPManifest.h \
    $${PWD}/OAICustomRPResourceTypeRouteDefinition.h \
    $${PWD}/OAICustomRPRouteDefinition.h \
    $${PWD}/OAICustomRPValidations.h \
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIListByCustomRPManifest.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceProviderOperation.h \
    $${PWD}/OAIResourceProviderOperationList.h \
    $${PWD}/OAIResourceProviderOperation_display.h \
    $${PWD}/OAIResourceProvidersUpdate.h \
# APIs
    $${PWD}/OAIAssociationsApi.h \
    $${PWD}/OAICustomResourceProviderApi.h \
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
    $${PWD}/OAIAssociation.cpp \
    $${PWD}/OAIAssociation_properties.cpp \
    $${PWD}/OAIAssociationsList.cpp \
    $${PWD}/OAICustomRPActionRouteDefinition.cpp \
    $${PWD}/OAICustomRPManifest.cpp \
    $${PWD}/OAICustomRPResourceTypeRouteDefinition.cpp \
    $${PWD}/OAICustomRPRouteDefinition.cpp \
    $${PWD}/OAICustomRPValidations.cpp \
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIListByCustomRPManifest.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceProviderOperation.cpp \
    $${PWD}/OAIResourceProviderOperationList.cpp \
    $${PWD}/OAIResourceProviderOperation_display.cpp \
    $${PWD}/OAIResourceProvidersUpdate.cpp \
# APIs
    $${PWD}/OAIAssociationsApi.cpp \
    $${PWD}/OAICustomResourceProviderApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
