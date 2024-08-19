QT += network

HEADERS += \
# Models
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response.h \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_declination.h \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_grid_variation.h \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_inclination.h \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_total_intensity.h \
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
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response.cpp \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_declination.cpp \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_grid_variation.cpp \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_inclination.cpp \
    $${PWD}/OAIApp_api_wmm_endpoints_WMM_magnetic_field_200_response_total_intensity.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
