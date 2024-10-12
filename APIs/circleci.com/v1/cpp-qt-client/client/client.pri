QT += network

HEADERS += \
# Models
    $${PWD}/OAIArtifact.h \
    $${PWD}/OAIAws.h \
    $${PWD}/OAIBuild.h \
    $${PWD}/OAIBuildDetail.h \
    $${PWD}/OAIBuildSummary.h \
    $${PWD}/OAICommitDetail.h \
    $${PWD}/OAIEnvvar.h \
    $${PWD}/OAIKey.h \
    $${PWD}/OAILifecycle.h \
    $${PWD}/OAIOutcome.h \
    $${PWD}/OAIPreviousBuild.h \
    $${PWD}/OAIProject.h \
    $${PWD}/OAIProject_feature_flags.h \
    $${PWD}/OAIScope.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITests.h \
    $${PWD}/OAITests_tests_inner.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAI_project__username___project__build_cache_delete_200_response.h \
    $${PWD}/OAI_project__username___project__checkout_key__fingerprint__delete_200_response.h \
    $${PWD}/OAI_project__username___project__post_request.h \
    $${PWD}/OAI_project__username___project__ssh_key_post_default_response.h \
    $${PWD}/OAI_project__username___project__ssh_key_post_request.h \
    $${PWD}/OAI_project__username___project__tree__branch__post_request.h \
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
    $${PWD}/OAIArtifact.cpp \
    $${PWD}/OAIAws.cpp \
    $${PWD}/OAIBuild.cpp \
    $${PWD}/OAIBuildDetail.cpp \
    $${PWD}/OAIBuildSummary.cpp \
    $${PWD}/OAICommitDetail.cpp \
    $${PWD}/OAIEnvvar.cpp \
    $${PWD}/OAIKey.cpp \
    $${PWD}/OAILifecycle.cpp \
    $${PWD}/OAIOutcome.cpp \
    $${PWD}/OAIPreviousBuild.cpp \
    $${PWD}/OAIProject.cpp \
    $${PWD}/OAIProject_feature_flags.cpp \
    $${PWD}/OAIScope.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITests.cpp \
    $${PWD}/OAITests_tests_inner.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAI_project__username___project__build_cache_delete_200_response.cpp \
    $${PWD}/OAI_project__username___project__checkout_key__fingerprint__delete_200_response.cpp \
    $${PWD}/OAI_project__username___project__post_request.cpp \
    $${PWD}/OAI_project__username___project__ssh_key_post_default_response.cpp \
    $${PWD}/OAI_project__username___project__ssh_key_post_request.cpp \
    $${PWD}/OAI_project__username___project__tree__branch__post_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
