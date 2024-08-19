QT += network

HEADERS += \
# Models
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_ambient_dose_200_response.h \
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_ambient_dose_200_response_dose_rate.h \
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_effective_dose_200_response.h \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_ambient_dose_200_response.h \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_ambient_dose_200_response_dose.h \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_effective_dose_200_response.h \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_ambient_dose_200_response.h \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_differential_intensity_200_response.h \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_differential_intensity_200_response_energies.h \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_effective_dose_200_response.h \
# APIs
    $${PWD}/OAICari7Api.h \
    $${PWD}/OAIParmaApi.h \
    $${PWD}/OAIRoutedoseApi.h \
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
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_ambient_dose_200_response.cpp \
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_ambient_dose_200_response_dose_rate.cpp \
    $${PWD}/OAIApp_api_cari7_endpoints_CARI7_effective_dose_200_response.cpp \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_ambient_dose_200_response.cpp \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_ambient_dose_200_response_dose.cpp \
    $${PWD}/OAIApp_api_icaro_endpoints_ICARO_effective_dose_200_response.cpp \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_ambient_dose_200_response.cpp \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_differential_intensity_200_response.cpp \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_differential_intensity_200_response_energies.cpp \
    $${PWD}/OAIApp_api_parma_endpoints_PARMA_effective_dose_200_response.cpp \
# APIs
    $${PWD}/OAICari7Api.cpp \
    $${PWD}/OAIParmaApi.cpp \
    $${PWD}/OAIRoutedoseApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
