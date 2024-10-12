QT += network

HEADERS += \
# Models
    $${PWD}/OAIAlternatePattern_inner.h \
    $${PWD}/OAIAnalysisRequest.h \
    $${PWD}/OAIAnalysisResponse.h \
    $${PWD}/OAICategoryPattern.h \
    $${PWD}/OAIClassPattern.h \
    $${PWD}/OAIContainerCategoryPattern.h \
    $${PWD}/OAIDrawingAttributesPattern.h \
    $${PWD}/OAIDrawingAttributesPattern_color.h \
    $${PWD}/OAIErrorModel.h \
    $${PWD}/OAIErrorModel_details_inner.h \
    $${PWD}/OAIInkPoint.h \
    $${PWD}/OAIInkPointValueAttribute.h \
    $${PWD}/OAILeafCategoryPattern.h \
    $${PWD}/OAIPointDetailsPattern.h \
    $${PWD}/OAIRecognitionUnit_inner.h \
    $${PWD}/OAIRecognitionUnit_inner_boundingRectangle.h \
    $${PWD}/OAIShapePattern.h \
    $${PWD}/OAIStroke.h \
# APIs
    $${PWD}/OAIInkRecognizerApi.h \
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
    $${PWD}/OAIAlternatePattern_inner.cpp \
    $${PWD}/OAIAnalysisRequest.cpp \
    $${PWD}/OAIAnalysisResponse.cpp \
    $${PWD}/OAICategoryPattern.cpp \
    $${PWD}/OAIClassPattern.cpp \
    $${PWD}/OAIContainerCategoryPattern.cpp \
    $${PWD}/OAIDrawingAttributesPattern.cpp \
    $${PWD}/OAIDrawingAttributesPattern_color.cpp \
    $${PWD}/OAIErrorModel.cpp \
    $${PWD}/OAIErrorModel_details_inner.cpp \
    $${PWD}/OAIInkPoint.cpp \
    $${PWD}/OAIInkPointValueAttribute.cpp \
    $${PWD}/OAILeafCategoryPattern.cpp \
    $${PWD}/OAIPointDetailsPattern.cpp \
    $${PWD}/OAIRecognitionUnit_inner.cpp \
    $${PWD}/OAIRecognitionUnit_inner_boundingRectangle.cpp \
    $${PWD}/OAIShapePattern.cpp \
    $${PWD}/OAIStroke.cpp \
# APIs
    $${PWD}/OAIInkRecognizerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
