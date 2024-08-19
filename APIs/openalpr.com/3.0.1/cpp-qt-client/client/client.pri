QT += network

HEADERS += \
# Models
    $${PWD}/OAICoordinate.h \
    $${PWD}/OAIGetConfig_200_response.h \
    $${PWD}/OAIGetConfig_200_response_countries_inner.h \
    $${PWD}/OAIGetConfig_200_response_vehicle_labels.h \
    $${PWD}/OAIPlate_candidate.h \
    $${PWD}/OAIPlate_details.h \
    $${PWD}/OAIRecognizeFile_200_response.h \
    $${PWD}/OAIRecognizeFile_200_response_processing_time.h \
    $${PWD}/OAIRecognizeFile_400_response.h \
    $${PWD}/OAIRegion_of_interest.h \
    $${PWD}/OAIVehicle_candidate.h \
    $${PWD}/OAIVehicle_details.h \
    $${PWD}/OAIVehicles.h \
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
    $${PWD}/OAICoordinate.cpp \
    $${PWD}/OAIGetConfig_200_response.cpp \
    $${PWD}/OAIGetConfig_200_response_countries_inner.cpp \
    $${PWD}/OAIGetConfig_200_response_vehicle_labels.cpp \
    $${PWD}/OAIPlate_candidate.cpp \
    $${PWD}/OAIPlate_details.cpp \
    $${PWD}/OAIRecognizeFile_200_response.cpp \
    $${PWD}/OAIRecognizeFile_200_response_processing_time.cpp \
    $${PWD}/OAIRecognizeFile_400_response.cpp \
    $${PWD}/OAIRegion_of_interest.cpp \
    $${PWD}/OAIVehicle_candidate.cpp \
    $${PWD}/OAIVehicle_details.cpp \
    $${PWD}/OAIVehicles.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
