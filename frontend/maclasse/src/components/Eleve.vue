<template>
  <div v-if="currentEleve" class="edit-form">
    <h4>Elève</h4>
    <form>
      <div class="form-group">
        <label for="nom">Nom</label>
        <input type="text" class="form-control" id="nom"
          v-model="currentEleve.nom"
        />
      </div>
      <div class="form-group">
        <label for="prenom">Prenom</label>
        <input type="text" class="form-control" id="prenom"
          v-model="currentEleve.prenom"
        />
      </div>
      <div class="form-group">
        <label for="date_naissance">Date de naissance</label>
        <input type="date" class="form-control" id="date_naissance"
          v-model="currentEleve.date_naissance"
        />
      </div>
      <div class="form-group">
        <label for="note_trimestre_1">Note du premier trimestre</label>
        <input type="number" class="form-control" id="note_trimestre_1"
          v-model="currentEleve.note_trimestre_1"
        />
      </div>
      <div class="form-group">
        <label for="note_trimestre_2">Note du deuxième trimestre</label>
        <input type="number" class="form-control" id="note_trimestre_2"
          v-model="currentEleve.note_trimestre_2"
        />
      </div>
      <div class="form-group">
        <label for="note_trimestre_3">Note du troisième trimestre</label>
        <input type="number" class="form-control" id="note_trimestre_3"
          v-model="currentEleve.note_trimestre_3"
        />
      </div>
    </form>


    <button class="badge badge-danger mr-2"
      @click="deleteEleve"
    >
      Supprimer
    </button>

    <button type="submit" class="badge badge-success"
      @click="updateEleve"
    >
      Modifier
    </button>
    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Cliquer sur un élève...</p>
  </div>
</template>

<script>
import EleveDataService from "../EleveDataService";

export default {
  name: "eleve",
  data() {
    return {
      currentEleve: null,
      message: ''
    };
  },
  methods: {
    getEleve(id) {
      EleveDataService.get(id)
        .then(response => {
          this.currentEleve = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updateEleve() {
      EleveDataService.update(this.currentEleve.id, this.currentEleve)
        .then(response => {
          console.log(response.data);
          this.message = 'Elève modifié !';
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteEleve() {
      EleveDataService.delete(this.currentEleve.id)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "eleves" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getEleve(this.$route.params.id);
  }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>