QT += network

HEADERS += \
# Models
    $${PWD}/OAIRegionHealth.h \
    $${PWD}/OAIRegionHealthList.h \
    $${PWD}/OAIRegionHealthModel.h \
    $${PWD}/OAIRegionHealthModel_alertSummary.h \
    $${PWD}/OAIRegionHealthModel_usageMetrics_inner.h \
    $${PWD}/OAIRegionHealthModel_usageMetrics_inner_metricsValue_inner.h \
# APIs
    $${PWD}/OAIRegionHealthsApi.h \
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
    $${PWD}/OAIRegionHealth.cpp \
    $${PWD}/OAIRegionHealthList.cpp \
    $${PWD}/OAIRegionHealthModel.cpp \
    $${PWD}/OAIRegionHealthModel_alertSummary.cpp \
    $${PWD}/OAIRegionHealthModel_usageMetrics_inner.cpp \
    $${PWD}/OAIRegionHealthModel_usageMetrics_inner_metricsValue_inner.cpp \
# APIs
    $${PWD}/OAIRegionHealthsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
