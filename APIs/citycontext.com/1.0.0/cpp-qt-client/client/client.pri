QT += network

HEADERS += \
# Models
    $${PWD}/OAILocation.h \
    $${PWD}/OAIPointInfo.h \
    $${PWD}/OAIPointInfo_lsoa.h \
    $${PWD}/OAIPointInfo_lsoa_population.h \
    $${PWD}/OAIPointInfo_parks_inner.h \
    $${PWD}/OAIPointInfo_schools_inner.h \
    $${PWD}/OAIUsage.h \
# APIs
    $${PWD}/OAICitycontextApi.h \
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
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIPointInfo.cpp \
    $${PWD}/OAIPointInfo_lsoa.cpp \
    $${PWD}/OAIPointInfo_lsoa_population.cpp \
    $${PWD}/OAIPointInfo_parks_inner.cpp \
    $${PWD}/OAIPointInfo_schools_inner.cpp \
    $${PWD}/OAIUsage.cpp \
# APIs
    $${PWD}/OAICitycontextApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
