QT += network

HEADERS += \
# Models
    $${PWD}/OAICloseApproachData.h \
    $${PWD}/OAIEstimatedDiameter.h \
    $${PWD}/OAIEstimatedDiameterContainer.h \
    $${PWD}/OAIMissDistance.h \
    $${PWD}/OAINearEarthObject.h \
    $${PWD}/OAINearEarthObjectList.h \
    $${PWD}/OAIOrbitClass.h \
    $${PWD}/OAIOrbitalData.h \
    $${PWD}/OAIPageMetaData.h \
    $${PWD}/OAIRelVelocity.h \
    $${PWD}/OAISentryImpactRiskObject.h \
    $${PWD}/OAISentryObjectPagingDto.h \
    $${PWD}/OAIStatistics.h \
    $${PWD}/OAIURL.h \
# APIs
    $${PWD}/OAIFeedApi.h \
    $${PWD}/OAINeoApi.h \
    $${PWD}/OAINeosentryApi.h \
    $${PWD}/OAIStatsApi.h \
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
    $${PWD}/OAICloseApproachData.cpp \
    $${PWD}/OAIEstimatedDiameter.cpp \
    $${PWD}/OAIEstimatedDiameterContainer.cpp \
    $${PWD}/OAIMissDistance.cpp \
    $${PWD}/OAINearEarthObject.cpp \
    $${PWD}/OAINearEarthObjectList.cpp \
    $${PWD}/OAIOrbitClass.cpp \
    $${PWD}/OAIOrbitalData.cpp \
    $${PWD}/OAIPageMetaData.cpp \
    $${PWD}/OAIRelVelocity.cpp \
    $${PWD}/OAISentryImpactRiskObject.cpp \
    $${PWD}/OAISentryObjectPagingDto.cpp \
    $${PWD}/OAIStatistics.cpp \
    $${PWD}/OAIURL.cpp \
# APIs
    $${PWD}/OAIFeedApi.cpp \
    $${PWD}/OAINeoApi.cpp \
    $${PWD}/OAINeosentryApi.cpp \
    $${PWD}/OAIStatsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
