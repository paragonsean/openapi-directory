QT += network

HEADERS += \
# Models
    $${PWD}/OAIAltLabel.h \
    $${PWD}/OAIAltLabelMode.h \
    $${PWD}/OAIDataItem.h \
    $${PWD}/OAIHierarchicalInterview.h \
    $${PWD}/OAIHierarchy.h \
    $${PWD}/OAIInterview.h \
    $${PWD}/OAILabel.h \
    $${PWD}/OAILanguage.h \
    $${PWD}/OAILevel.h \
    $${PWD}/OAIParentDetails.h \
    $${PWD}/OAIParentRef.h \
    $${PWD}/OAIParentType.h \
    $${PWD}/OAISurveyDetail.h \
    $${PWD}/OAISurveyMetadata.h \
    $${PWD}/OAISurveyMetadataBase.h \
    $${PWD}/OAIUseType.h \
    $${PWD}/OAIValue.h \
    $${PWD}/OAIValueRange.h \
    $${PWD}/OAIVariable.h \
    $${PWD}/OAIVariableType.h \
    $${PWD}/OAIVariableValues.h \
# APIs
    $${PWD}/OAISurveysApi.h \
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
    $${PWD}/OAIAltLabel.cpp \
    $${PWD}/OAIAltLabelMode.cpp \
    $${PWD}/OAIDataItem.cpp \
    $${PWD}/OAIHierarchicalInterview.cpp \
    $${PWD}/OAIHierarchy.cpp \
    $${PWD}/OAIInterview.cpp \
    $${PWD}/OAILabel.cpp \
    $${PWD}/OAILanguage.cpp \
    $${PWD}/OAILevel.cpp \
    $${PWD}/OAIParentDetails.cpp \
    $${PWD}/OAIParentRef.cpp \
    $${PWD}/OAIParentType.cpp \
    $${PWD}/OAISurveyDetail.cpp \
    $${PWD}/OAISurveyMetadata.cpp \
    $${PWD}/OAISurveyMetadataBase.cpp \
    $${PWD}/OAIUseType.cpp \
    $${PWD}/OAIValue.cpp \
    $${PWD}/OAIValueRange.cpp \
    $${PWD}/OAIVariable.cpp \
    $${PWD}/OAIVariableType.cpp \
    $${PWD}/OAIVariableValues.cpp \
# APIs
    $${PWD}/OAISurveysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
