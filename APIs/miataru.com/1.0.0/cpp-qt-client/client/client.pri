QT += network

HEADERS += \
# Models
    $${PWD}/OAIACK.h \
    $${PWD}/OAIMiataruGetLocationDevice.h \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse.h \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse_geometry.h \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse_properties.h \
    $${PWD}/OAIMiataruGetLocationHistoryRequest.h \
    $${PWD}/OAIMiataruGetLocationHistoryRequest_MiataruConfig.h \
    $${PWD}/OAIMiataruGetLocationHistoryRequest_MiataruGetLocationHistory.h \
    $${PWD}/OAIMiataruGetLocationHistoryResponse.h \
    $${PWD}/OAIMiataruGetLocationHistoryResponse_MiataruServerConfig.h \
    $${PWD}/OAIMiataruGetLocationRequest.h \
    $${PWD}/OAIMiataruGetLocationResponse.h \
    $${PWD}/OAIMiataruGetVisitorHistoryRequest.h \
    $${PWD}/OAIMiataruGetVisitorHistoryRequest_MiataruGetVisitorHistory.h \
    $${PWD}/OAIMiataruGetVisitorHistoryResponse.h \
    $${PWD}/OAIMiataruGetVisitorHistoryResponse_MiataruServerConfig.h \
    $${PWD}/OAIMiataruLocation.h \
    $${PWD}/OAIMiataruUpdateLocationRequest.h \
    $${PWD}/OAIMiataruUpdateLocationRequest_MiataruConfig.h \
    $${PWD}/OAIMiataruVisitors.h \
# APIs
    $${PWD}/OAIGetLocationApi.h \
    $${PWD}/OAIGetVisitorHistoryApi.h \
    $${PWD}/OAIUpdateLocationApi.h \
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
    $${PWD}/OAIACK.cpp \
    $${PWD}/OAIMiataruGetLocationDevice.cpp \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse.cpp \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse_geometry.cpp \
    $${PWD}/OAIMiataruGetLocationGeoJSONResponse_properties.cpp \
    $${PWD}/OAIMiataruGetLocationHistoryRequest.cpp \
    $${PWD}/OAIMiataruGetLocationHistoryRequest_MiataruConfig.cpp \
    $${PWD}/OAIMiataruGetLocationHistoryRequest_MiataruGetLocationHistory.cpp \
    $${PWD}/OAIMiataruGetLocationHistoryResponse.cpp \
    $${PWD}/OAIMiataruGetLocationHistoryResponse_MiataruServerConfig.cpp \
    $${PWD}/OAIMiataruGetLocationRequest.cpp \
    $${PWD}/OAIMiataruGetLocationResponse.cpp \
    $${PWD}/OAIMiataruGetVisitorHistoryRequest.cpp \
    $${PWD}/OAIMiataruGetVisitorHistoryRequest_MiataruGetVisitorHistory.cpp \
    $${PWD}/OAIMiataruGetVisitorHistoryResponse.cpp \
    $${PWD}/OAIMiataruGetVisitorHistoryResponse_MiataruServerConfig.cpp \
    $${PWD}/OAIMiataruLocation.cpp \
    $${PWD}/OAIMiataruUpdateLocationRequest.cpp \
    $${PWD}/OAIMiataruUpdateLocationRequest_MiataruConfig.cpp \
    $${PWD}/OAIMiataruVisitors.cpp \
# APIs
    $${PWD}/OAIGetLocationApi.cpp \
    $${PWD}/OAIGetVisitorHistoryApi.cpp \
    $${PWD}/OAIUpdateLocationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
