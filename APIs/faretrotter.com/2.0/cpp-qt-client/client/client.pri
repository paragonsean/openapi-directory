QT += network

HEADERS += \
# Models
    $${PWD}/OAIPlaceResponse.h \
    $${PWD}/OAIPlacesResponse.h \
    $${PWD}/OAIPlacesResponse_request.h \
    $${PWD}/OAIPlacesResponse_request_fields.h \
    $${PWD}/OAIPlacesResponse_status.h \
    $${PWD}/OAIRoutesResponse.h \
    $${PWD}/OAIRoutesResponse_data.h \
    $${PWD}/OAIRoutesResponse_data_operators_inner.h \
    $${PWD}/OAIRoutesResponse_data_routes_inner.h \
    $${PWD}/OAIRoutesResponse_response.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIPlaceResponse.cpp \
    $${PWD}/OAIPlacesResponse.cpp \
    $${PWD}/OAIPlacesResponse_request.cpp \
    $${PWD}/OAIPlacesResponse_request_fields.cpp \
    $${PWD}/OAIPlacesResponse_status.cpp \
    $${PWD}/OAIRoutesResponse.cpp \
    $${PWD}/OAIRoutesResponse_data.cpp \
    $${PWD}/OAIRoutesResponse_data_operators_inner.cpp \
    $${PWD}/OAIRoutesResponse_data_routes_inner.cpp \
    $${PWD}/OAIRoutesResponse_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
