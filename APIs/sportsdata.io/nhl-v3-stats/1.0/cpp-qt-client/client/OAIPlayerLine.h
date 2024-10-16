/**
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayerLine.h
 *
 * 
 */

#ifndef OAIPlayerLine_H
#define OAIPlayerLine_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlayerLine : public OAIObject {
public:
    OAIPlayerLine();
    OAIPlayerLine(QString json);
    ~OAIPlayerLine() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getLineNumber() const;
    void setLineNumber(const qint32 &line_number);
    bool is_line_number_Set() const;
    bool is_line_number_Valid() const;

    QString getLineType() const;
    void setLineType(const QString &line_type);
    bool is_line_type_Set() const;
    bool is_line_type_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    QString getPosition() const;
    void setPosition(const QString &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getShoots() const;
    void setShoots(const QString &shoots);
    bool is_shoots_Set() const;
    bool is_shoots_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_line_number;
    bool m_line_number_isSet;
    bool m_line_number_isValid;

    QString m_line_type;
    bool m_line_type_isSet;
    bool m_line_type_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_shoots;
    bool m_shoots_isSet;
    bool m_shoots_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayerLine)

#endif // OAIPlayerLine_H
