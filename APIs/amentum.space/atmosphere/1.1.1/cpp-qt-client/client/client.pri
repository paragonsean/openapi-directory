QT += network

HEADERS += \
# Models
    $${PWD}/OAIApp_api_endpoints_JB2008_sample_atmosphere_200_response.h \
    $${PWD}/OAIApp_api_endpoints_JB2008_sample_atmosphere_200_response_at_alt_temp.h \
    $${PWD}/OAIApp_api_endpoints_NRLMSISE00_sample_atmosphere_200_response.h \
    $${PWD}/OAIApp_api_endpoints_NRLMSISE00_sample_atmosphere_200_response_ap.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_N2_density.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_O2_density.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_O_density.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_eastward_wind_neutral.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_northward_wind_neutral.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_point.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_temp_neutral.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_total_mass_density.h \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_upward_wind_neutral.h \
# APIs
    $${PWD}/OAIJb2008Api.h \
    $${PWD}/OAINrlmsise00Api.h \
    $${PWD}/OAIWamIpeApi.h \
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
    $${PWD}/OAIApp_api_endpoints_JB2008_sample_atmosphere_200_response.cpp \
    $${PWD}/OAIApp_api_endpoints_JB2008_sample_atmosphere_200_response_at_alt_temp.cpp \
    $${PWD}/OAIApp_api_endpoints_NRLMSISE00_sample_atmosphere_200_response.cpp \
    $${PWD}/OAIApp_api_endpoints_NRLMSISE00_sample_atmosphere_200_response_ap.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_N2_density.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_O2_density.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_O_density.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_eastward_wind_neutral.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_northward_wind_neutral.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_point.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_temp_neutral.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_total_mass_density.cpp \
    $${PWD}/OAIApp_api_wfs_endpoints_WFS_get_values_200_response_upward_wind_neutral.cpp \
# APIs
    $${PWD}/OAIJb2008Api.cpp \
    $${PWD}/OAINrlmsise00Api.cpp \
    $${PWD}/OAIWamIpeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
