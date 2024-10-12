QT += network

HEADERS += \
# Models
    $${PWD}/OAIGroundhog.h \
    $${PWD}/OAIGroundhog_200_response.h \
    $${PWD}/OAIGroundhog_400_response.h \
    $${PWD}/OAIGroundhog_400_response_error.h \
    $${PWD}/OAIGroundhogs_200_response.h \
    $${PWD}/OAIPrediction.h \
    $${PWD}/OAIPredictions_200_response.h \
    $${PWD}/OAIPredictions_400_response.h \
    $${PWD}/OAIRoot_200_response.h \
    $${PWD}/OAIRoot_200_response__links.h \
    $${PWD}/OAIRoot_200_response__links_groundhog.h \
# APIs
    $${PWD}/OAIGroundhogsApi.h \
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAIPredictionsApi.h \
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
    $${PWD}/OAIGroundhog.cpp \
    $${PWD}/OAIGroundhog_200_response.cpp \
    $${PWD}/OAIGroundhog_400_response.cpp \
    $${PWD}/OAIGroundhog_400_response_error.cpp \
    $${PWD}/OAIGroundhogs_200_response.cpp \
    $${PWD}/OAIPrediction.cpp \
    $${PWD}/OAIPredictions_200_response.cpp \
    $${PWD}/OAIPredictions_400_response.cpp \
    $${PWD}/OAIRoot_200_response.cpp \
    $${PWD}/OAIRoot_200_response__links.cpp \
    $${PWD}/OAIRoot_200_response__links_groundhog.cpp \
# APIs
    $${PWD}/OAIGroundhogsApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAIPredictionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
