QT += network

HEADERS += \
# Models
    $${PWD}/OAIVolume.h \
    $${PWD}/OAIVolumeList.h \
    $${PWD}/OAIVolumeModel.h \
# APIs
    $${PWD}/OAIVolumesApi.h \
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
    $${PWD}/OAIVolume.cpp \
    $${PWD}/OAIVolumeList.cpp \
    $${PWD}/OAIVolumeModel.cpp \
# APIs
    $${PWD}/OAIVolumesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
