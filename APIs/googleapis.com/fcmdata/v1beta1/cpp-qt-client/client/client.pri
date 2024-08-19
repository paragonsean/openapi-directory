QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1AndroidDeliveryData.h \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1Data.h \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1DeliveryPerformancePercents.h \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse.h \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1MessageInsightPercents.h \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1MessageOutcomePercents.h \
    $${PWD}/OAIGoogleTypeDate.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1AndroidDeliveryData.cpp \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1Data.cpp \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1DeliveryPerformancePercents.cpp \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse.cpp \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1MessageInsightPercents.cpp \
    $${PWD}/OAIGoogleFirebaseFcmDataV1beta1MessageOutcomePercents.cpp \
    $${PWD}/OAIGoogleTypeDate.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
