QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnomaly.h \
    $${PWD}/OAIAnomaly_eta.h \
    $${PWD}/OAIAnomaly_gravity_anomaly.h \
    $${PWD}/OAIAnomaly_xi.h \
    $${PWD}/OAIHeight.h \
    $${PWD}/OAIHeight_height.h \
# APIs
    $${PWD}/OAIEgm2008Api.h \
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
    $${PWD}/OAIAnomaly.cpp \
    $${PWD}/OAIAnomaly_eta.cpp \
    $${PWD}/OAIAnomaly_gravity_anomaly.cpp \
    $${PWD}/OAIAnomaly_xi.cpp \
    $${PWD}/OAIHeight.cpp \
    $${PWD}/OAIHeight_height.cpp \
# APIs
    $${PWD}/OAIEgm2008Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
