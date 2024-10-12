QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorFieldContract.h \
    $${PWD}/OAIWorkbookError.h \
    $${PWD}/OAIWorkbookTemplate.h \
    $${PWD}/OAIWorkbookTemplateGallery.h \
    $${PWD}/OAIWorkbookTemplateLocalizedGallery.h \
    $${PWD}/OAIWorkbookTemplateProperties.h \
    $${PWD}/OAIWorkbookTemplateResource.h \
    $${PWD}/OAIWorkbookTemplateUpdateParameters.h \
    $${PWD}/OAIWorkbookTemplatesListResult.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIErrorFieldContract.cpp \
    $${PWD}/OAIWorkbookError.cpp \
    $${PWD}/OAIWorkbookTemplate.cpp \
    $${PWD}/OAIWorkbookTemplateGallery.cpp \
    $${PWD}/OAIWorkbookTemplateLocalizedGallery.cpp \
    $${PWD}/OAIWorkbookTemplateProperties.cpp \
    $${PWD}/OAIWorkbookTemplateResource.cpp \
    $${PWD}/OAIWorkbookTemplateUpdateParameters.cpp \
    $${PWD}/OAIWorkbookTemplatesListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
