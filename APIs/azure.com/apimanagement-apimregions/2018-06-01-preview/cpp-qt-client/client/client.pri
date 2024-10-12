QT += network

HEADERS += \
# Models
    $${PWD}/OAIRegion_ListByService_200_response.h \
    $${PWD}/OAIRegion_ListByService_200_response_value_inner.h \
    $${PWD}/OAIRegion_ListByService_default_response.h \
    $${PWD}/OAIRegion_ListByService_default_response_error.h \
    $${PWD}/OAIRegion_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIRegionApi.h \
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
    $${PWD}/OAIRegion_ListByService_200_response.cpp \
    $${PWD}/OAIRegion_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIRegion_ListByService_default_response.cpp \
    $${PWD}/OAIRegion_ListByService_default_response_error.cpp \
    $${PWD}/OAIRegion_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIRegionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
