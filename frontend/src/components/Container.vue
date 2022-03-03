<template>
  <div class="row">
  <div class="col-lg-6"></div>
  <div class="col-lg-6">
    <table class="table">
      <thead>
        <th>Id</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Edit</th>
        <th>Delete</th>
      </thead>
      <tbody>
        <tr v-for="contact in contacts" v-bind:key="contact.id">
          <td>{{contact.id}}</td>
          <td>{{contact.name}}</td>
          <td>{{contact.email}}</td>
          <td>{{contact.phone}}</td>
          <td>
            <button @click="getOne(contact)" class="btn bn-sm btn-success"><i class="fa fa-pencil"></i></button>
          </td>
          <td>
            <button @click="getOne(contact)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Contact-Container',
  props: {
    msg: String
  },
  data(){
    return{
      contacts: null,
      name: '',
      email: '',
      phone: ''
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/contacts/')
      .then((res)=>{
        this.contacts=res.data
      })
    },
    getOne(contact){
      this.name = contact.name;
    }
  }
}
</script>

<style scoped>

</style>
