<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="nom">Nom</label>
        <input
          type="text"
          class="form-control"
          id="nom"
          required
          v-model="eleve.nom"
          name="nom"
        />
      </div>

      <div class="form-group">
        <label for="prenom">Prenom</label>
        <input
          type="text"
          class="form-control"
          id="prenom"
          required
          v-model="eleve.prenom"
          name="prenom"
        />
      </div>

      <div class="form-group">
        <label for="date_naissance">Date de naissance</label>
        <input
          type="date"
          class="form-control"
          id="date_naissance"
          required
          v-model="eleve.date_naissance"
          name="date_naissance"
        />
      </div>

      <div class="form-group">
        <label for="note_trimestre_1">Note du premier trimestre</label>
        <input
          type="number"
          class="form-control"
          id="note_trimestre_1"
          required
          v-model="eleve.note_trimestre_1"
          name="note_trimestre_1"
        />
      </div>

      <div class="form-group">
        <label for="note_trimestre_2">Note du deuxième trimestre</label>
        <input
          type="number"
          class="form-control"
          id="note_trimestre_2"
          required
          v-model="eleve.note_trimestre_2"
          name="note_trimestre_2"
        />
      </div>

      <div class="form-group">
        <label for="note_trimestre_3">Note du troisème trimestre</label>
        <input
          type="number"
          class="form-control"
          id="note_trimestre_3"
          required
          v-model="eleve.note_trimestre_3"
          name="note_trimestre_3"
        />
      </div>

      <button @click="saveEleve" class="btn btn-success">Envoyer</button>
    </div>

    <div v-else>
      <h4>Elève ajouté !</h4>
      <button class="btn btn-success" @click="newEleve">Ajouter un autre élève</button>
      <router-link to="/eleves" class="nav-link">Liste des élèves</router-link>
    </div>
  </div>
</template>

<script>
import EleveDataService from "../EleveDataService";

export default {
  name: "add-eleve",
  data() {
    return {
      eleve: {
        id: null,
        nom: "",
        prenom: "",
        date_naissance: "",
        note_trimestre_1: null,
        note_trimestre_2: null,
        note_trimestre_3: null
      },
      submitted: false
    };
  },
  methods: {
    saveEleve() {
      var data = {
        nom: this.eleve.nom,
        prenom: this.eleve.prenom,
        date_naissance: this.eleve.date_naissance,
        note_trimestre_1: this.eleve.note_trimestre_1,
        note_trimestre_2: this.eleve.note_trimestre_2,
        note_trimestre_3: this.eleve.note_trimestre_3,
      };

      EleveDataService.create(data)
        .then(response => {
          this.eleve.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },

    newEleve() {
      this.submitted = false;
      this.eleve = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>