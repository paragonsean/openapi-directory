/*
 * LoL v3 Stats
 * LoL v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Champion
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:14.423769-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Champion {
  public static final String SERIALIZED_NAME_ARMOR = "Armor";
  @SerializedName(SERIALIZED_NAME_ARMOR)
  private BigDecimal armor;

  public static final String SERIALIZED_NAME_ARMOR_PER_LEVEL = "ArmorPerLevel";
  @SerializedName(SERIALIZED_NAME_ARMOR_PER_LEVEL)
  private BigDecimal armorPerLevel;

  public static final String SERIALIZED_NAME_ATTACK = "Attack";
  @SerializedName(SERIALIZED_NAME_ATTACK)
  private BigDecimal attack;

  public static final String SERIALIZED_NAME_ATTACK_DAMAGE = "AttackDamage";
  @SerializedName(SERIALIZED_NAME_ATTACK_DAMAGE)
  private BigDecimal attackDamage;

  public static final String SERIALIZED_NAME_ATTACK_DAMAGE_PER_LEVEL = "AttackDamagePerLevel";
  @SerializedName(SERIALIZED_NAME_ATTACK_DAMAGE_PER_LEVEL)
  private BigDecimal attackDamagePerLevel;

  public static final String SERIALIZED_NAME_ATTACK_RANGE = "AttackRange";
  @SerializedName(SERIALIZED_NAME_ATTACK_RANGE)
  private BigDecimal attackRange;

  public static final String SERIALIZED_NAME_ATTACK_SPEED_OFFSET = "AttackSpeedOffset";
  @SerializedName(SERIALIZED_NAME_ATTACK_SPEED_OFFSET)
  private BigDecimal attackSpeedOffset;

  public static final String SERIALIZED_NAME_CHAMPION_ID = "ChampionId";
  @SerializedName(SERIALIZED_NAME_CHAMPION_ID)
  private Integer championId;

  public static final String SERIALIZED_NAME_DEFENSE = "Defense";
  @SerializedName(SERIALIZED_NAME_DEFENSE)
  private BigDecimal defense;

  public static final String SERIALIZED_NAME_DIFFICULTY = "Difficulty";
  @SerializedName(SERIALIZED_NAME_DIFFICULTY)
  private BigDecimal difficulty;

  public static final String SERIALIZED_NAME_HP = "Hp";
  @SerializedName(SERIALIZED_NAME_HP)
  private BigDecimal hp;

  public static final String SERIALIZED_NAME_HP_REGEN = "HpRegen";
  @SerializedName(SERIALIZED_NAME_HP_REGEN)
  private BigDecimal hpRegen;

  public static final String SERIALIZED_NAME_HP_REGEN_PER_LEVEL = "HpRegenPerLevel";
  @SerializedName(SERIALIZED_NAME_HP_REGEN_PER_LEVEL)
  private BigDecimal hpRegenPerLevel;

  public static final String SERIALIZED_NAME_HP_UP_PER_LEVEL = "HpUpPerLevel";
  @SerializedName(SERIALIZED_NAME_HP_UP_PER_LEVEL)
  private BigDecimal hpUpPerLevel;

  public static final String SERIALIZED_NAME_MAGIC = "Magic";
  @SerializedName(SERIALIZED_NAME_MAGIC)
  private BigDecimal magic;

  public static final String SERIALIZED_NAME_MOVE_SPEED = "MoveSpeed";
  @SerializedName(SERIALIZED_NAME_MOVE_SPEED)
  private BigDecimal moveSpeed;

  public static final String SERIALIZED_NAME_MP = "Mp";
  @SerializedName(SERIALIZED_NAME_MP)
  private BigDecimal mp;

  public static final String SERIALIZED_NAME_MP_REGEN = "MpRegen";
  @SerializedName(SERIALIZED_NAME_MP_REGEN)
  private BigDecimal mpRegen;

  public static final String SERIALIZED_NAME_MP_REGEN_PER_LEVEL = "MpRegenPerLevel";
  @SerializedName(SERIALIZED_NAME_MP_REGEN_PER_LEVEL)
  private BigDecimal mpRegenPerLevel;

  public static final String SERIALIZED_NAME_MP_UP_PER_LEVEL = "MpUpPerLevel";
  @SerializedName(SERIALIZED_NAME_MP_UP_PER_LEVEL)
  private BigDecimal mpUpPerLevel;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SPELL_BLOCK = "SpellBlock";
  @SerializedName(SERIALIZED_NAME_SPELL_BLOCK)
  private BigDecimal spellBlock;

  public static final String SERIALIZED_NAME_SPELL_BLOCK_PER_LEVEL = "SpellBlockPerLevel";
  @SerializedName(SERIALIZED_NAME_SPELL_BLOCK_PER_LEVEL)
  private BigDecimal spellBlockPerLevel;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public Champion() {
  }

  public Champion armor(BigDecimal armor) {
    this.armor = armor;
    return this;
  }

  /**
   * Get armor
   * @return armor
   */
  @javax.annotation.Nullable
  public BigDecimal getArmor() {
    return armor;
  }

  public void setArmor(BigDecimal armor) {
    this.armor = armor;
  }


  public Champion armorPerLevel(BigDecimal armorPerLevel) {
    this.armorPerLevel = armorPerLevel;
    return this;
  }

  /**
   * Get armorPerLevel
   * @return armorPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getArmorPerLevel() {
    return armorPerLevel;
  }

  public void setArmorPerLevel(BigDecimal armorPerLevel) {
    this.armorPerLevel = armorPerLevel;
  }


  public Champion attack(BigDecimal attack) {
    this.attack = attack;
    return this;
  }

  /**
   * Get attack
   * @return attack
   */
  @javax.annotation.Nullable
  public BigDecimal getAttack() {
    return attack;
  }

  public void setAttack(BigDecimal attack) {
    this.attack = attack;
  }


  public Champion attackDamage(BigDecimal attackDamage) {
    this.attackDamage = attackDamage;
    return this;
  }

  /**
   * Get attackDamage
   * @return attackDamage
   */
  @javax.annotation.Nullable
  public BigDecimal getAttackDamage() {
    return attackDamage;
  }

  public void setAttackDamage(BigDecimal attackDamage) {
    this.attackDamage = attackDamage;
  }


  public Champion attackDamagePerLevel(BigDecimal attackDamagePerLevel) {
    this.attackDamagePerLevel = attackDamagePerLevel;
    return this;
  }

  /**
   * Get attackDamagePerLevel
   * @return attackDamagePerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getAttackDamagePerLevel() {
    return attackDamagePerLevel;
  }

  public void setAttackDamagePerLevel(BigDecimal attackDamagePerLevel) {
    this.attackDamagePerLevel = attackDamagePerLevel;
  }


  public Champion attackRange(BigDecimal attackRange) {
    this.attackRange = attackRange;
    return this;
  }

  /**
   * Get attackRange
   * @return attackRange
   */
  @javax.annotation.Nullable
  public BigDecimal getAttackRange() {
    return attackRange;
  }

  public void setAttackRange(BigDecimal attackRange) {
    this.attackRange = attackRange;
  }


  public Champion attackSpeedOffset(BigDecimal attackSpeedOffset) {
    this.attackSpeedOffset = attackSpeedOffset;
    return this;
  }

  /**
   * Get attackSpeedOffset
   * @return attackSpeedOffset
   */
  @javax.annotation.Nullable
  public BigDecimal getAttackSpeedOffset() {
    return attackSpeedOffset;
  }

  public void setAttackSpeedOffset(BigDecimal attackSpeedOffset) {
    this.attackSpeedOffset = attackSpeedOffset;
  }


  public Champion championId(Integer championId) {
    this.championId = championId;
    return this;
  }

  /**
   * Get championId
   * @return championId
   */
  @javax.annotation.Nullable
  public Integer getChampionId() {
    return championId;
  }

  public void setChampionId(Integer championId) {
    this.championId = championId;
  }


  public Champion defense(BigDecimal defense) {
    this.defense = defense;
    return this;
  }

  /**
   * Get defense
   * @return defense
   */
  @javax.annotation.Nullable
  public BigDecimal getDefense() {
    return defense;
  }

  public void setDefense(BigDecimal defense) {
    this.defense = defense;
  }


  public Champion difficulty(BigDecimal difficulty) {
    this.difficulty = difficulty;
    return this;
  }

  /**
   * Get difficulty
   * @return difficulty
   */
  @javax.annotation.Nullable
  public BigDecimal getDifficulty() {
    return difficulty;
  }

  public void setDifficulty(BigDecimal difficulty) {
    this.difficulty = difficulty;
  }


  public Champion hp(BigDecimal hp) {
    this.hp = hp;
    return this;
  }

  /**
   * Get hp
   * @return hp
   */
  @javax.annotation.Nullable
  public BigDecimal getHp() {
    return hp;
  }

  public void setHp(BigDecimal hp) {
    this.hp = hp;
  }


  public Champion hpRegen(BigDecimal hpRegen) {
    this.hpRegen = hpRegen;
    return this;
  }

  /**
   * Get hpRegen
   * @return hpRegen
   */
  @javax.annotation.Nullable
  public BigDecimal getHpRegen() {
    return hpRegen;
  }

  public void setHpRegen(BigDecimal hpRegen) {
    this.hpRegen = hpRegen;
  }


  public Champion hpRegenPerLevel(BigDecimal hpRegenPerLevel) {
    this.hpRegenPerLevel = hpRegenPerLevel;
    return this;
  }

  /**
   * Get hpRegenPerLevel
   * @return hpRegenPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getHpRegenPerLevel() {
    return hpRegenPerLevel;
  }

  public void setHpRegenPerLevel(BigDecimal hpRegenPerLevel) {
    this.hpRegenPerLevel = hpRegenPerLevel;
  }


  public Champion hpUpPerLevel(BigDecimal hpUpPerLevel) {
    this.hpUpPerLevel = hpUpPerLevel;
    return this;
  }

  /**
   * Get hpUpPerLevel
   * @return hpUpPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getHpUpPerLevel() {
    return hpUpPerLevel;
  }

  public void setHpUpPerLevel(BigDecimal hpUpPerLevel) {
    this.hpUpPerLevel = hpUpPerLevel;
  }


  public Champion magic(BigDecimal magic) {
    this.magic = magic;
    return this;
  }

  /**
   * Get magic
   * @return magic
   */
  @javax.annotation.Nullable
  public BigDecimal getMagic() {
    return magic;
  }

  public void setMagic(BigDecimal magic) {
    this.magic = magic;
  }


  public Champion moveSpeed(BigDecimal moveSpeed) {
    this.moveSpeed = moveSpeed;
    return this;
  }

  /**
   * Get moveSpeed
   * @return moveSpeed
   */
  @javax.annotation.Nullable
  public BigDecimal getMoveSpeed() {
    return moveSpeed;
  }

  public void setMoveSpeed(BigDecimal moveSpeed) {
    this.moveSpeed = moveSpeed;
  }


  public Champion mp(BigDecimal mp) {
    this.mp = mp;
    return this;
  }

  /**
   * Get mp
   * @return mp
   */
  @javax.annotation.Nullable
  public BigDecimal getMp() {
    return mp;
  }

  public void setMp(BigDecimal mp) {
    this.mp = mp;
  }


  public Champion mpRegen(BigDecimal mpRegen) {
    this.mpRegen = mpRegen;
    return this;
  }

  /**
   * Get mpRegen
   * @return mpRegen
   */
  @javax.annotation.Nullable
  public BigDecimal getMpRegen() {
    return mpRegen;
  }

  public void setMpRegen(BigDecimal mpRegen) {
    this.mpRegen = mpRegen;
  }


  public Champion mpRegenPerLevel(BigDecimal mpRegenPerLevel) {
    this.mpRegenPerLevel = mpRegenPerLevel;
    return this;
  }

  /**
   * Get mpRegenPerLevel
   * @return mpRegenPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getMpRegenPerLevel() {
    return mpRegenPerLevel;
  }

  public void setMpRegenPerLevel(BigDecimal mpRegenPerLevel) {
    this.mpRegenPerLevel = mpRegenPerLevel;
  }


  public Champion mpUpPerLevel(BigDecimal mpUpPerLevel) {
    this.mpUpPerLevel = mpUpPerLevel;
    return this;
  }

  /**
   * Get mpUpPerLevel
   * @return mpUpPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getMpUpPerLevel() {
    return mpUpPerLevel;
  }

  public void setMpUpPerLevel(BigDecimal mpUpPerLevel) {
    this.mpUpPerLevel = mpUpPerLevel;
  }


  public Champion name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Champion spellBlock(BigDecimal spellBlock) {
    this.spellBlock = spellBlock;
    return this;
  }

  /**
   * Get spellBlock
   * @return spellBlock
   */
  @javax.annotation.Nullable
  public BigDecimal getSpellBlock() {
    return spellBlock;
  }

  public void setSpellBlock(BigDecimal spellBlock) {
    this.spellBlock = spellBlock;
  }


  public Champion spellBlockPerLevel(BigDecimal spellBlockPerLevel) {
    this.spellBlockPerLevel = spellBlockPerLevel;
    return this;
  }

  /**
   * Get spellBlockPerLevel
   * @return spellBlockPerLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getSpellBlockPerLevel() {
    return spellBlockPerLevel;
  }

  public void setSpellBlockPerLevel(BigDecimal spellBlockPerLevel) {
    this.spellBlockPerLevel = spellBlockPerLevel;
  }


  public Champion title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Champion champion = (Champion) o;
    return Objects.equals(this.armor, champion.armor) &&
        Objects.equals(this.armorPerLevel, champion.armorPerLevel) &&
        Objects.equals(this.attack, champion.attack) &&
        Objects.equals(this.attackDamage, champion.attackDamage) &&
        Objects.equals(this.attackDamagePerLevel, champion.attackDamagePerLevel) &&
        Objects.equals(this.attackRange, champion.attackRange) &&
        Objects.equals(this.attackSpeedOffset, champion.attackSpeedOffset) &&
        Objects.equals(this.championId, champion.championId) &&
        Objects.equals(this.defense, champion.defense) &&
        Objects.equals(this.difficulty, champion.difficulty) &&
        Objects.equals(this.hp, champion.hp) &&
        Objects.equals(this.hpRegen, champion.hpRegen) &&
        Objects.equals(this.hpRegenPerLevel, champion.hpRegenPerLevel) &&
        Objects.equals(this.hpUpPerLevel, champion.hpUpPerLevel) &&
        Objects.equals(this.magic, champion.magic) &&
        Objects.equals(this.moveSpeed, champion.moveSpeed) &&
        Objects.equals(this.mp, champion.mp) &&
        Objects.equals(this.mpRegen, champion.mpRegen) &&
        Objects.equals(this.mpRegenPerLevel, champion.mpRegenPerLevel) &&
        Objects.equals(this.mpUpPerLevel, champion.mpUpPerLevel) &&
        Objects.equals(this.name, champion.name) &&
        Objects.equals(this.spellBlock, champion.spellBlock) &&
        Objects.equals(this.spellBlockPerLevel, champion.spellBlockPerLevel) &&
        Objects.equals(this.title, champion.title);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(armor, armorPerLevel, attack, attackDamage, attackDamagePerLevel, attackRange, attackSpeedOffset, championId, defense, difficulty, hp, hpRegen, hpRegenPerLevel, hpUpPerLevel, magic, moveSpeed, mp, mpRegen, mpRegenPerLevel, mpUpPerLevel, name, spellBlock, spellBlockPerLevel, title);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Champion {\n");
    sb.append("    armor: ").append(toIndentedString(armor)).append("\n");
    sb.append("    armorPerLevel: ").append(toIndentedString(armorPerLevel)).append("\n");
    sb.append("    attack: ").append(toIndentedString(attack)).append("\n");
    sb.append("    attackDamage: ").append(toIndentedString(attackDamage)).append("\n");
    sb.append("    attackDamagePerLevel: ").append(toIndentedString(attackDamagePerLevel)).append("\n");
    sb.append("    attackRange: ").append(toIndentedString(attackRange)).append("\n");
    sb.append("    attackSpeedOffset: ").append(toIndentedString(attackSpeedOffset)).append("\n");
    sb.append("    championId: ").append(toIndentedString(championId)).append("\n");
    sb.append("    defense: ").append(toIndentedString(defense)).append("\n");
    sb.append("    difficulty: ").append(toIndentedString(difficulty)).append("\n");
    sb.append("    hp: ").append(toIndentedString(hp)).append("\n");
    sb.append("    hpRegen: ").append(toIndentedString(hpRegen)).append("\n");
    sb.append("    hpRegenPerLevel: ").append(toIndentedString(hpRegenPerLevel)).append("\n");
    sb.append("    hpUpPerLevel: ").append(toIndentedString(hpUpPerLevel)).append("\n");
    sb.append("    magic: ").append(toIndentedString(magic)).append("\n");
    sb.append("    moveSpeed: ").append(toIndentedString(moveSpeed)).append("\n");
    sb.append("    mp: ").append(toIndentedString(mp)).append("\n");
    sb.append("    mpRegen: ").append(toIndentedString(mpRegen)).append("\n");
    sb.append("    mpRegenPerLevel: ").append(toIndentedString(mpRegenPerLevel)).append("\n");
    sb.append("    mpUpPerLevel: ").append(toIndentedString(mpUpPerLevel)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    spellBlock: ").append(toIndentedString(spellBlock)).append("\n");
    sb.append("    spellBlockPerLevel: ").append(toIndentedString(spellBlockPerLevel)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("Armor");
    openapiFields.add("ArmorPerLevel");
    openapiFields.add("Attack");
    openapiFields.add("AttackDamage");
    openapiFields.add("AttackDamagePerLevel");
    openapiFields.add("AttackRange");
    openapiFields.add("AttackSpeedOffset");
    openapiFields.add("ChampionId");
    openapiFields.add("Defense");
    openapiFields.add("Difficulty");
    openapiFields.add("Hp");
    openapiFields.add("HpRegen");
    openapiFields.add("HpRegenPerLevel");
    openapiFields.add("HpUpPerLevel");
    openapiFields.add("Magic");
    openapiFields.add("MoveSpeed");
    openapiFields.add("Mp");
    openapiFields.add("MpRegen");
    openapiFields.add("MpRegenPerLevel");
    openapiFields.add("MpUpPerLevel");
    openapiFields.add("Name");
    openapiFields.add("SpellBlock");
    openapiFields.add("SpellBlockPerLevel");
    openapiFields.add("Title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Champion
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Champion.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Champion is not found in the empty JSON string", Champion.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Champion.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Champion` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Title") != null && !jsonObj.get("Title").isJsonNull()) && !jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Champion.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Champion' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Champion> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Champion.class));

       return (TypeAdapter<T>) new TypeAdapter<Champion>() {
           @Override
           public void write(JsonWriter out, Champion value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Champion read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Champion given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Champion
   * @throws IOException if the JSON string is invalid with respect to Champion
   */
  public static Champion fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Champion.class);
  }

  /**
   * Convert an instance of Champion to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

