QT += network

HEADERS += \
# Models
    $${PWD}/OAIAncestorReference.h \
    $${PWD}/OAIAspect.h \
    $${PWD}/OAIAspectConstraint.h \
    $${PWD}/OAIAspectMetadata.h \
    $${PWD}/OAIAspectValue.h \
    $${PWD}/OAIBaseCategoryTree.h \
    $${PWD}/OAICategory.h \
    $${PWD}/OAICategoryAspect.h \
    $${PWD}/OAICategorySubtree.h \
    $${PWD}/OAICategorySuggestion.h \
    $${PWD}/OAICategorySuggestionResponse.h \
    $${PWD}/OAICategoryTree.h \
    $${PWD}/OAICategoryTreeNode.h \
    $${PWD}/OAICompatibilityProperty.h \
    $${PWD}/OAICompatibilityPropertyValue.h \
    $${PWD}/OAIGetCategoriesAspectResponse.h \
    $${PWD}/OAIGetCompatibilityMetadataResponse.h \
    $${PWD}/OAIGetCompatibilityPropertyValuesResponse.h \
    $${PWD}/OAIRelevanceIndicator.h \
    $${PWD}/OAIValueConstraint.h \
# APIs
    $${PWD}/OAICategoryTreeApi.h \
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
    $${PWD}/OAIAncestorReference.cpp \
    $${PWD}/OAIAspect.cpp \
    $${PWD}/OAIAspectConstraint.cpp \
    $${PWD}/OAIAspectMetadata.cpp \
    $${PWD}/OAIAspectValue.cpp \
    $${PWD}/OAIBaseCategoryTree.cpp \
    $${PWD}/OAICategory.cpp \
    $${PWD}/OAICategoryAspect.cpp \
    $${PWD}/OAICategorySubtree.cpp \
    $${PWD}/OAICategorySuggestion.cpp \
    $${PWD}/OAICategorySuggestionResponse.cpp \
    $${PWD}/OAICategoryTree.cpp \
    $${PWD}/OAICategoryTreeNode.cpp \
    $${PWD}/OAICompatibilityProperty.cpp \
    $${PWD}/OAICompatibilityPropertyValue.cpp \
    $${PWD}/OAIGetCategoriesAspectResponse.cpp \
    $${PWD}/OAIGetCompatibilityMetadataResponse.cpp \
    $${PWD}/OAIGetCompatibilityPropertyValuesResponse.cpp \
    $${PWD}/OAIRelevanceIndicator.cpp \
    $${PWD}/OAIValueConstraint.cpp \
# APIs
    $${PWD}/OAICategoryTreeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
