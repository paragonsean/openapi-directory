/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectPersistVO.h
 *
 * Java type: com.noosh.domain.nooshapi.persist.vo.ProjectPersistVO
 */

#ifndef OAIProjectPersistVO_H
#define OAIProjectPersistVO_H

#include <QJsonObject>

#include "OAICustomFieldPersistVO.h"
#include <QDate>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomFieldPersistVO;

class OAIProjectPersistVO : public OAIObject {
public:
    OAIProjectPersistVO();
    OAIProjectPersistVO(QString json);
    ~OAIProjectPersistVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClientAccount() const;
    void setClientAccount(const QString &client_account);
    bool is_client_account_Set() const;
    bool is_client_account_Valid() const;

    qint64 getClientUserId() const;
    void setClientUserId(const qint64 &client_user_id);
    bool is_client_user_id_Set() const;
    bool is_client_user_id_Valid() const;

    qint64 getClientWorkgroupId() const;
    void setClientWorkgroupId(const qint64 &client_workgroup_id);
    bool is_client_workgroup_id_Set() const;
    bool is_client_workgroup_id_Valid() const;

    QString getComments() const;
    void setComments(const QString &comments);
    bool is_comments_Set() const;
    bool is_comments_Valid() const;

    QDate getCompletionDate() const;
    void setCompletionDate(const QDate &completion_date);
    bool is_completion_date_Set() const;
    bool is_completion_date_Valid() const;

    QList<OAICustomFieldPersistVO> getCustomFields() const;
    void setCustomFields(const QList<OAICustomFieldPersistVO> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    qint64 getDeactivationReasonId() const;
    void setDeactivationReasonId(const qint64 &deactivation_reason_id);
    bool is_deactivation_reason_id_Set() const;
    bool is_deactivation_reason_id_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsHot() const;
    void setIsHot(const bool &is_hot);
    bool is_is_hot_Set() const;
    bool is_is_hot_Valid() const;

    bool isIsPaperDirect() const;
    void setIsPaperDirect(const bool &is_paper_direct);
    bool is_is_paper_direct_Set() const;
    bool is_is_paper_direct_Valid() const;

    qint64 getProjectCategoryId() const;
    void setProjectCategoryId(const qint64 &project_category_id);
    bool is_project_category_id_Set() const;
    bool is_project_category_id_Valid() const;

    QString getProjectDescription() const;
    void setProjectDescription(const QString &project_description);
    bool is_project_description_Set() const;
    bool is_project_description_Valid() const;

    QString getProjectName() const;
    void setProjectName(const QString &project_name);
    bool is_project_name_Set() const;
    bool is_project_name_Valid() const;

    QString getProjectNumber() const;
    void setProjectNumber(const QString &project_number);
    bool is_project_number_Set() const;
    bool is_project_number_Valid() const;

    qint64 getProjectOwnerUserId() const;
    void setProjectOwnerUserId(const qint64 &project_owner_user_id);
    bool is_project_owner_user_id_Set() const;
    bool is_project_owner_user_id_Valid() const;

    qint64 getProjectStatusId() const;
    void setProjectStatusId(const qint64 &project_status_id);
    bool is_project_status_id_Set() const;
    bool is_project_status_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_client_account;
    bool m_client_account_isSet;
    bool m_client_account_isValid;

    qint64 m_client_user_id;
    bool m_client_user_id_isSet;
    bool m_client_user_id_isValid;

    qint64 m_client_workgroup_id;
    bool m_client_workgroup_id_isSet;
    bool m_client_workgroup_id_isValid;

    QString m_comments;
    bool m_comments_isSet;
    bool m_comments_isValid;

    QDate m_completion_date;
    bool m_completion_date_isSet;
    bool m_completion_date_isValid;

    QList<OAICustomFieldPersistVO> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    qint64 m_deactivation_reason_id;
    bool m_deactivation_reason_id_isSet;
    bool m_deactivation_reason_id_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_hot;
    bool m_is_hot_isSet;
    bool m_is_hot_isValid;

    bool m_is_paper_direct;
    bool m_is_paper_direct_isSet;
    bool m_is_paper_direct_isValid;

    qint64 m_project_category_id;
    bool m_project_category_id_isSet;
    bool m_project_category_id_isValid;

    QString m_project_description;
    bool m_project_description_isSet;
    bool m_project_description_isValid;

    QString m_project_name;
    bool m_project_name_isSet;
    bool m_project_name_isValid;

    QString m_project_number;
    bool m_project_number_isSet;
    bool m_project_number_isValid;

    qint64 m_project_owner_user_id;
    bool m_project_owner_user_id_isSet;
    bool m_project_owner_user_id_isValid;

    qint64 m_project_status_id;
    bool m_project_status_id_isSet;
    bool m_project_status_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectPersistVO)

#endif // OAIProjectPersistVO_H
