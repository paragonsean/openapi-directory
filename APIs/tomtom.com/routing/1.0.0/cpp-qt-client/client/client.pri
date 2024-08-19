QT += network

HEADERS += \
# Models
    $${PWD}/OAICalculateReachableRangePostDataParameters.h \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas.h \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas_rectangles_inner.h \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas_rectangles_inner_northEastCorner.h \
    $${PWD}/OAICalculateRoutePostDataParameters.h \
    $${PWD}/OAICalculateRoutePostDataParameters_supportingPoints_inner.h \
# APIs
    $${PWD}/OAIRoutingApi.h \
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
    $${PWD}/OAICalculateReachableRangePostDataParameters.cpp \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas.cpp \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas_rectangles_inner.cpp \
    $${PWD}/OAICalculateReachableRangePostDataParameters_avoidAreas_rectangles_inner_northEastCorner.cpp \
    $${PWD}/OAICalculateRoutePostDataParameters.cpp \
    $${PWD}/OAICalculateRoutePostDataParameters_supportingPoints_inner.cpp \
# APIs
    $${PWD}/OAIRoutingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
