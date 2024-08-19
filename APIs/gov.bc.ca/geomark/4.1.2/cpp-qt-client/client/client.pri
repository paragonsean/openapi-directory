QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIBoundingBoxApi.h \
    $${PWD}/OAICreateApi.h \
    $${PWD}/OAIFeatureApi.h \
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAIPartsApi.h \
    $${PWD}/OAIPointApi.h \
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
# APIs
    $${PWD}/OAIBoundingBoxApi.cpp \
    $${PWD}/OAICreateApi.cpp \
    $${PWD}/OAIFeatureApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAIPartsApi.cpp \
    $${PWD}/OAIPointApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
