QT += network

HEADERS += \
# Models
    $${PWD}/OAIArea.h \
    $${PWD}/OAIBasemapZOrder.h \
    $${PWD}/OAIExtrudedArea.h \
    $${PWD}/OAIFeature.h \
    $${PWD}/OAIFeatureTile.h \
    $${PWD}/OAIFirstDerivativeElevationGrid.h \
    $${PWD}/OAIGeometry.h \
    $${PWD}/OAILine.h \
    $${PWD}/OAIModeledVolume.h \
    $${PWD}/OAIProviderInfo.h \
    $${PWD}/OAIRelation.h \
    $${PWD}/OAIRoadInfo.h \
    $${PWD}/OAIRow.h \
    $${PWD}/OAISecondDerivativeElevationGrid.h \
    $${PWD}/OAISegmentInfo.h \
    $${PWD}/OAITerrainTile.h \
    $${PWD}/OAITileCoordinates.h \
    $${PWD}/OAITriangleStrip.h \
    $${PWD}/OAIVertex2DList.h \
    $${PWD}/OAIVertex3DList.h \
# APIs
    $${PWD}/OAITerraintilesApi.h \
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
    $${PWD}/OAIArea.cpp \
    $${PWD}/OAIBasemapZOrder.cpp \
    $${PWD}/OAIExtrudedArea.cpp \
    $${PWD}/OAIFeature.cpp \
    $${PWD}/OAIFeatureTile.cpp \
    $${PWD}/OAIFirstDerivativeElevationGrid.cpp \
    $${PWD}/OAIGeometry.cpp \
    $${PWD}/OAILine.cpp \
    $${PWD}/OAIModeledVolume.cpp \
    $${PWD}/OAIProviderInfo.cpp \
    $${PWD}/OAIRelation.cpp \
    $${PWD}/OAIRoadInfo.cpp \
    $${PWD}/OAIRow.cpp \
    $${PWD}/OAISecondDerivativeElevationGrid.cpp \
    $${PWD}/OAISegmentInfo.cpp \
    $${PWD}/OAITerrainTile.cpp \
    $${PWD}/OAITileCoordinates.cpp \
    $${PWD}/OAITriangleStrip.cpp \
    $${PWD}/OAIVertex2DList.cpp \
    $${PWD}/OAIVertex3DList.cpp \
# APIs
    $${PWD}/OAITerraintilesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
