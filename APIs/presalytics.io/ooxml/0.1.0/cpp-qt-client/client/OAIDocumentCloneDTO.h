/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDocumentCloneDTO.h
 *
 * 
 */

#ifndef OAIDocumentCloneDTO_H
#define OAIDocumentCloneDTO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDocumentCloneDTO : public OAIObject {
public:
    OAIDocumentCloneDTO();
    OAIDocumentCloneDTO(QString json);
    ~OAIDocumentCloneDTO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getStoryId() const;
    void setStoryId(const QString &story_id);
    bool is_story_id_Set() const;
    bool is_story_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_story_id;
    bool m_story_id_isSet;
    bool m_story_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDocumentCloneDTO)

#endif // OAIDocumentCloneDTO_H
