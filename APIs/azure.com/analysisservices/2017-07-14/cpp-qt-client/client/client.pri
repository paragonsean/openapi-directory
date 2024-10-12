QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnalysisServicesServer.h \
    $${PWD}/OAIAnalysisServicesServerMutableProperties.h \
    $${PWD}/OAIAnalysisServicesServerProperties.h \
    $${PWD}/OAIAnalysisServicesServerUpdateParameters.h \
    $${PWD}/OAIAnalysisServicesServers.h \
    $${PWD}/OAICheckServerNameAvailabilityParameters.h \
    $${PWD}/OAICheckServerNameAvailabilityResult.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIGatewayDetails.h \
    $${PWD}/OAIGatewayError.h \
    $${PWD}/OAIGatewayListStatusError.h \
    $${PWD}/OAIGatewayListStatusLive.h \
    $${PWD}/OAIOperationStatus.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceSku.h \
    $${PWD}/OAIServerAdministrators.h \
    $${PWD}/OAISkuDetailsForExistingResource.h \
    $${PWD}/OAISkuEnumerationForExistingResourceResult.h \
    $${PWD}/OAISkuEnumerationForNewResourceResult.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIServersApi.h \
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
    $${PWD}/OAIAnalysisServicesServer.cpp \
    $${PWD}/OAIAnalysisServicesServerMutableProperties.cpp \
    $${PWD}/OAIAnalysisServicesServerProperties.cpp \
    $${PWD}/OAIAnalysisServicesServerUpdateParameters.cpp \
    $${PWD}/OAIAnalysisServicesServers.cpp \
    $${PWD}/OAICheckServerNameAvailabilityParameters.cpp \
    $${PWD}/OAICheckServerNameAvailabilityResult.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIGatewayDetails.cpp \
    $${PWD}/OAIGatewayError.cpp \
    $${PWD}/OAIGatewayListStatusError.cpp \
    $${PWD}/OAIGatewayListStatusLive.cpp \
    $${PWD}/OAIOperationStatus.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceSku.cpp \
    $${PWD}/OAIServerAdministrators.cpp \
    $${PWD}/OAISkuDetailsForExistingResource.cpp \
    $${PWD}/OAISkuEnumerationForExistingResourceResult.cpp \
    $${PWD}/OAISkuEnumerationForNewResourceResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
