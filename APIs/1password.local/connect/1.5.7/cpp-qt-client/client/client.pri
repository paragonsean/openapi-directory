QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIRequest.h \
    $${PWD}/OAIAPIRequest_actor.h \
    $${PWD}/OAIAPIRequest_resource.h \
    $${PWD}/OAIAPIRequest_resource_item.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIField.h \
    $${PWD}/OAIField_section.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIFile_section.h \
    $${PWD}/OAIFullItem.h \
    $${PWD}/OAIFullItem_allOf_sections.h \
    $${PWD}/OAIGeneratorRecipe.h \
    $${PWD}/OAIGetServerHealth_200_response.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItem_urls_inner.h \
    $${PWD}/OAIItem_vault.h \
    $${PWD}/OAIPatch_inner.h \
    $${PWD}/OAIServiceDependency.h \
    $${PWD}/OAIVault.h \
# APIs
    $${PWD}/OAIActivityApi.h \
    $${PWD}/OAIFilesApi.h \
    $${PWD}/OAIHealthApi.h \
    $${PWD}/OAIItemsApi.h \
    $${PWD}/OAIMetricsApi.h \
    $${PWD}/OAIVaultsApi.h \
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
    $${PWD}/OAIAPIRequest.cpp \
    $${PWD}/OAIAPIRequest_actor.cpp \
    $${PWD}/OAIAPIRequest_resource.cpp \
    $${PWD}/OAIAPIRequest_resource_item.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIField.cpp \
    $${PWD}/OAIField_section.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIFile_section.cpp \
    $${PWD}/OAIFullItem.cpp \
    $${PWD}/OAIFullItem_allOf_sections.cpp \
    $${PWD}/OAIGeneratorRecipe.cpp \
    $${PWD}/OAIGetServerHealth_200_response.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItem_urls_inner.cpp \
    $${PWD}/OAIItem_vault.cpp \
    $${PWD}/OAIPatch_inner.cpp \
    $${PWD}/OAIServiceDependency.cpp \
    $${PWD}/OAIVault.cpp \
# APIs
    $${PWD}/OAIActivityApi.cpp \
    $${PWD}/OAIFilesApi.cpp \
    $${PWD}/OAIHealthApi.cpp \
    $${PWD}/OAIItemsApi.cpp \
    $${PWD}/OAIMetricsApi.cpp \
    $${PWD}/OAIVaultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
