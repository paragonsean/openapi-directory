QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleMapsPlayablelocationsV3Impression.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3LogImpressionsRequest.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3LogPlayerReportsRequest.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3PlayerReport.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleAreaFilter.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleCriterion.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleFilter.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocation.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationList.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse.h \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleSpacingOptions.h \
    $${PWD}/OAIGoogleMapsUnityClientInfo.h \
    $${PWD}/OAIGoogleTypeLatLng.h \
# APIs
    $${PWD}/OAIV3Api.h \
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
    $${PWD}/OAIGoogleMapsPlayablelocationsV3Impression.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3LogImpressionsRequest.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3LogPlayerReportsRequest.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3PlayerReport.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleAreaFilter.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleCriterion.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleFilter.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocation.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationList.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse.cpp \
    $${PWD}/OAIGoogleMapsPlayablelocationsV3SampleSpacingOptions.cpp \
    $${PWD}/OAIGoogleMapsUnityClientInfo.cpp \
    $${PWD}/OAIGoogleTypeLatLng.cpp \
# APIs
    $${PWD}/OAIV3Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
