QT += network

HEADERS += \
# Models
    $${PWD}/OAIBaselineMetadata.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIMetricBaselinesProperties.h \
    $${PWD}/OAIMetricBaselinesResponse.h \
    $${PWD}/OAIMetricSingleDimension.h \
    $${PWD}/OAISingleBaseline.h \
    $${PWD}/OAISingleMetricBaseline.h \
    $${PWD}/OAITimeSeriesBaseline.h \
# APIs
    $${PWD}/OAIBaselineApi.h \
    $${PWD}/OAIMetricApi.h \
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
    $${PWD}/OAIBaselineMetadata.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIMetricBaselinesProperties.cpp \
    $${PWD}/OAIMetricBaselinesResponse.cpp \
    $${PWD}/OAIMetricSingleDimension.cpp \
    $${PWD}/OAISingleBaseline.cpp \
    $${PWD}/OAISingleMetricBaseline.cpp \
    $${PWD}/OAITimeSeriesBaseline.cpp \
# APIs
    $${PWD}/OAIBaselineApi.cpp \
    $${PWD}/OAIMetricApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
