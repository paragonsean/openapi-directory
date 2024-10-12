/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApi_Core_Dto_Groups_Group.h
 *
 * 
 */

#ifndef OAIApi_Core_Dto_Groups_Group_H
#define OAIApi_Core_Dto_Groups_Group_H

#include <QJsonObject>

#include "OAIApi_Core_Dto_Tags_Tag.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApi_Core_Dto_Tags_Tag;

class OAIApi_Core_Dto_Groups_Group : public OAIObject {
public:
    OAIApi_Core_Dto_Groups_Group();
    OAIApi_Core_Dto_Groups_Group(QString json);
    ~OAIApi_Core_Dto_Groups_Group() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreationDate() const;
    void setCreationDate(const QString &creation_date);
    bool is_creation_date_Set() const;
    bool is_creation_date_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsPublic() const;
    void setIsPublic(const bool &is_public);
    bool is_is_public_Set() const;
    bool is_is_public_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    bool isPreferred() const;
    void setPreferred(const bool &preferred);
    bool is_preferred_Set() const;
    bool is_preferred_Valid() const;

    bool isRedirectOnly() const;
    void setRedirectOnly(const bool &redirect_only);
    bool is_redirect_only_Set() const;
    bool is_redirect_only_Valid() const;

    QList<OAIApi_Core_Dto_Tags_Tag> getTags() const;
    void setTags(const QList<OAIApi_Core_Dto_Tags_Tag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    bool isWritePermited() const;
    void setWritePermited(const bool &write_permited);
    bool is_write_permited_Set() const;
    bool is_write_permited_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_creation_date;
    bool m_creation_date_isSet;
    bool m_creation_date_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_public;
    bool m_is_public_isSet;
    bool m_is_public_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    bool m_preferred;
    bool m_preferred_isSet;
    bool m_preferred_isValid;

    bool m_redirect_only;
    bool m_redirect_only_isSet;
    bool m_redirect_only_isValid;

    QList<OAIApi_Core_Dto_Tags_Tag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    bool m_write_permited;
    bool m_write_permited_isSet;
    bool m_write_permited_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApi_Core_Dto_Groups_Group)

#endif // OAIApi_Core_Dto_Groups_Group_H
