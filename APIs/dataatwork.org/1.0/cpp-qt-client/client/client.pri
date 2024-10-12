QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIJob.h \
    $${PWD}/OAIJobRelatedJob.h \
    $${PWD}/OAIJobRelatedJobs.h \
    $${PWD}/OAIJobSkill.h \
    $${PWD}/OAIJobSkills.h \
    $${PWD}/OAIJobs.h \
    $${PWD}/OAINormalizedJob.h \
    $${PWD}/OAINormalizedSkill.h \
    $${PWD}/OAIPageLink.h \
    $${PWD}/OAISkill.h \
    $${PWD}/OAISkillJob.h \
    $${PWD}/OAISkillJobs.h \
    $${PWD}/OAISkillRelatedSkill.h \
    $${PWD}/OAISkillRelatedSkills.h \
    $${PWD}/OAISkills.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIJob.cpp \
    $${PWD}/OAIJobRelatedJob.cpp \
    $${PWD}/OAIJobRelatedJobs.cpp \
    $${PWD}/OAIJobSkill.cpp \
    $${PWD}/OAIJobSkills.cpp \
    $${PWD}/OAIJobs.cpp \
    $${PWD}/OAINormalizedJob.cpp \
    $${PWD}/OAINormalizedSkill.cpp \
    $${PWD}/OAIPageLink.cpp \
    $${PWD}/OAISkill.cpp \
    $${PWD}/OAISkillJob.cpp \
    $${PWD}/OAISkillJobs.cpp \
    $${PWD}/OAISkillRelatedSkill.cpp \
    $${PWD}/OAISkillRelatedSkills.cpp \
    $${PWD}/OAISkills.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
